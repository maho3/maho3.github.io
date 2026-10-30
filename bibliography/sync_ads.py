"""Sync content/publication/ with an ADS library.

Fetches every paper in the library, then writes each one's index.md and
cite.bib. Existing folders are matched by DOI, arXiv id or title, so their
slugs, featured.png and hand-edited fields (tags, image, url_* ...) are kept.
Folders that match nothing are reported, not deleted.

Token: $ADS_API_TOKEN, $ADS_DEV_KEY, or bibliography/SECRET_BIBTEX.

    conda run -n cv-ads python bibliography/sync_ads.py
"""

import html
import json
import os
import re
import sys
import unicodedata
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBS = ROOT / "content" / "publication"
BIB_OUT = ROOT / "bibliography" / "publications_ads.bib"
TOKEN_FILE = ROOT / "bibliography" / "SECRET_BIBTEX"

API = "https://api.adsabs.harvard.edu/v1"
LIBRARY_ID = "sSuEkJWCTZOuBEciWPiNuw"
FIELDS = "bibcode,title,author,pub,pubdate,doi,identifier,abstract,keyword,doctype"

# Library records that aren't papers
IGNORE = {"2026ascl.soft06020P", "2024ascl.soft03011H"}
# Shown under Featured Publications
FEATURED = {"2025MLS&T...6c5010H", "2024OJAp....7E..54H", "2022NatAs...6..936H",
            "2023MNRAS.524.3289H"}
# Hand-written folders for papers not on ADS; never touched or reported
MANUAL = {"zhang-2026-celia", "tirapongprasert-2026-agentic"}

ME = ("Ho", "M", "Matthew Ho")  # surname, initial, name of content/authors/ folder

# Front matter keys whose existing values are kept over the generated ones
KEEP = ["author_notes", "summary", "tags", "url_pdf", "url_code", "url_dataset",
        "url_poster", "url_project", "url_slides", "url_source", "url_video",
        "image", "projects"]

DOCTYPES = {"article": "article-journal", "inproceedings": "paper-conference",
            "eprint": "article"}


# ----------------------------------------------------------------- ADS ---

def token():
    tok = os.environ.get("ADS_API_TOKEN") or os.environ.get("ADS_DEV_KEY")
    if not tok and TOKEN_FILE.exists():
        tok = TOKEN_FILE.read_text().strip()
    if not tok:
        sys.exit("No ADS token: set $ADS_API_TOKEN or write it to bibliography/SECRET_BIBTEX.")
    return tok


def call(path, data=None, content_type="application/json"):
    req = urllib.request.Request(f"{API}{path}", data=data)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    if data is not None:
        req.add_header("Content-Type", content_type)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def library():
    bibcodes, start = [], 0
    while True:
        out = call(f"/biblib/libraries/{LIBRARY_ID}?start={start}&rows=100")
        bibcodes += out["documents"]
        start += 100
        if start >= out["metadata"]["num_documents"]:
            return [b for b in bibcodes if b not in IGNORE]


def records(bibcodes):
    data = ("bibcode\n" + "\n".join(bibcodes)).encode()
    out = call(f"/search/bigquery?q=*:*&rows=2000&fl={FIELDS}", data, "big-query/csv")
    return out["response"]["docs"]


def bibtex(bibcodes):
    """Combined BibTeX export, and each entry keyed by bibcode."""
    out = call("/export/bibtex", json.dumps({"bibcode": bibcodes}).encode())["export"]
    entries = {}
    for chunk in re.split(r"\n(?=@)", out.strip()):
        m = re.match(r"@\w+\{([^,]+),", chunk)
        if m:
            entries[m.group(1)] = chunk.strip() + "\n"
    return out, entries


# ------------------------------------------------------------ matching ---

def fold(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def plain(s):
    s = re.sub(r"\\text(?:tt|it|bf|rm)\{([^}]*)\}", r"\1", s)
    return html.unescape(re.sub(r"</?\w+>", "", s))


def arxiv_id(doc):
    return next((x.split(":", 1)[1] for x in doc.get("identifier", [])
                 if x.lower().startswith("arxiv:")), "")


def keys_of(doc):
    """Identifiers that can link an ADS record to an existing folder."""
    keys = {"title:" + fold(plain(doc["title"][0]))[:60]}
    keys |= {"doi:" + d.lower() for d in doc.get("doi", [])}
    if arxiv_id(doc):
        keys.add("arxiv:" + arxiv_id(doc))
    return keys


def folder_keys(folder):
    keys = set()
    for name in ("index.md", "cite.bib"):
        f = folder / name
        if not f.exists():
            continue
        text = f.read_text()
        for m in re.finditer(r"^\s*doi\s*[:=]\s*[{'\"]?([^}'\"\s,]+)", text, re.M | re.I):
            keys.add("doi:" + m.group(1).lower())
        for m in re.finditer(r"eprint\s*=\s*\{([^}]+)\}|arXiv[:.]?\s*(\d{4}\.\d{4,5})", text):
            keys.add("arxiv:" + (m.group(1) or m.group(2)))
        m = re.search(r"^\s*title\s*=\s*\{(.+?)\},?$", text, re.M)
        if m:
            keys.add("title:" + fold(re.sub(r"[{}]", "", m.group(1)))[:60])
    fm = front_matter(folder / "index.md")
    if "title" in fm:
        title = " ".join(l.strip() for l in fm["title"]).removeprefix("title:")
        keys.add("title:" + fold(title.strip(" '\""))[:60])
    return keys


def merge_preprints(docs):
    """Drop arXiv records that duplicate a published one in the library,
    keeping their arXiv id on the published record."""
    by_title = {}
    for d in docs:
        by_title.setdefault(fold(plain(d["title"][0])), []).append(d)
    out = []
    for group in by_title.values():
        published = [d for d in group if d.get("doctype") != "eprint"]
        if published and len(group) > 1:
            for d in published:
                d["identifier"] = d.get("identifier", []) + [
                    x for e in group if e not in published for x in e.get("identifier", [])]
            group = published
        out += group
    return out


def slug(doc, taken):
    surname = fold(doc["author"][0].split(",")[0])
    words = [fold(w) for w in plain(doc["title"][0]).split()]
    word = next((w for w in words if len(w) > 3 and w not in
                 {"learning", "universe", "with", "from", "using", "towards"}), words[0])
    base = s = f"{surname}-{doc['pubdate'][:4]}-{word}"
    n = 2
    while s in taken:
        s, n = f"{base}-{n}", n + 1
    return s


# --------------------------------------------------------- front matter ---

def front_matter(path):
    """Top-level front matter blocks: {key: [lines]}, comments dropped."""
    if not path.exists():
        return {}
    parts = path.read_text().split("---\n")
    blocks, key = {}, None
    for line in (parts[1] if len(parts) > 2 else "").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        m = re.match(r"^([A-Za-z_]+):", line)
        if m:
            key = m.group(1)
            blocks[key] = [line]
        elif key:
            blocks[key].append(line)
    return blocks


def is_empty(lines):
    return re.fullmatch(r"\w+:\s*(''|\"\"|\[\])?\s*", "\n".join(lines)) is not None


def author_name(a):
    last, _, first = a.partition(",")
    first = first.strip()
    if fold(last) == fold(ME[0]) and first[:1].upper() == ME[1]:
        return ME[2]
    return f"{first} {last.strip()}".strip()


def q(s):
    return json.dumps(s, ensure_ascii=False)


def render(doc, old, featured):
    date = doc["pubdate"].replace("-00", "-01")
    published = old.get("publishDate") or [
        f"publishDate: {q(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}"]
    links = [f"https://ui.adsabs.harvard.edu/abs/{doc['bibcode']}/abstract"]
    gen = {
        "title": [f"title: {q(plain(doc['title'][0]))}"],
        "authors": ["authors:"] + [f"- {q(author_name(a))}" for a in doc["author"]],
        "author_notes": ["author_notes: []"],
        "date": [f"date: {q(date)}"],
        "publishDate": published,
        "publication_types": ["publication_types:",
                              f"- {DOCTYPES.get(doc.get('doctype'), 'article-journal')}"],
        "publication": [f"publication: {q('*' + plain(doc.get('pub', '')) + '*')}"],
        "publication_short": ["publication_short: ''"],
        "doi": [f"doi: {q(doc['doi'][0])}"] if doc.get("doi") else [],
        "abstract": [f"abstract: {q(plain(doc.get('abstract', '')))}"],
        "summary": ["summary: ''"],
        "tags": ["tags:"] + [f"- {q(k)}" for k in doc.get("keyword", [])]
                if doc.get("keyword") else ["tags: []"],
        "featured": [f"featured: {'true' if featured else 'false'}"],
        "url_pdf": [f"url_pdf: {q('https://arxiv.org/abs/' + arxiv_id(doc))}"
                    if arxiv_id(doc) else "url_pdf: ''"],
        "links": ["links:", "- name: ADS", f"  url: {q(links[0])}"],
        "image": ["image:", "  caption: ''", "  focal_point: ''", "  preview_only: false"],
        "projects": ["projects: []"],
    }
    for k in KEEP:
        if k in old and not is_empty(old[k]):
            gen[k] = old[k]
    return "---\n" + "\n".join(l for v in gen.values() for l in v) + "\n---\n"


# ----------------------------------------------------------------- main ---

def main():
    bibcodes = library()
    docs = merge_preprints(records(bibcodes))
    docs.sort(key=lambda d: d["pubdate"], reverse=True)
    combined, entries = bibtex([d["bibcode"] for d in docs])
    BIB_OUT.write_text(combined)

    folders = {f.name: f for f in sorted(PUBS.iterdir())
               if f.is_dir() and f.name not in MANUAL}
    fkeys = {name: folder_keys(f) for name, f in folders.items()}
    used, created, updated = set(), [], []

    for doc in docs:
        matches = [n for n, k in fkeys.items() if k & keys_of(doc) and n not in used]
        # Prefer the folder with a featured image, then one named after the first author
        surname = fold(doc["author"][0].split(",")[0])
        matches.sort(key=lambda n: (not (folders[n] / "featured.png").exists(),
                                    not n.startswith(surname), n))
        if matches:
            name = matches[0]
            updated.append(name)
        else:
            name = slug(doc, set(folders) | used | MANUAL)
            created.append(name)
        used.add(name)
        folder = PUBS / name
        folder.mkdir(exist_ok=True)
        old = front_matter(folder / "index.md")
        (folder / "index.md").write_text(render(doc, old, doc["bibcode"] in FEATURED))
        if doc["bibcode"] in entries:
            (folder / "cite.bib").write_text(entries[doc["bibcode"]])

    missing = FEATURED - {d["bibcode"] for d in docs}
    print(f"{len(docs)} ADS records: {len(updated)} updated, {len(created)} created")
    for name in created:
        print(f"  new: {name}")
    for name in sorted(set(folders) - used):
        print(f"  unmatched (delete?): {name}")
    for b in sorted(missing):
        print(f"  FEATURED bibcode not in library: {b}")


if __name__ == "__main__":
    TOKEN = token()
    main()
