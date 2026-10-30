# Personal Website

Welcome to my personal website!  
Visit: [maho3.github.io](https://maho3.github.io)

---

## To Build

```bash
hugo server -D
```
Make sure you have `Hugo==0.136.6` extended installed ([link](https://github.com/gohugoio/hugo/releases/tag/v0.136.5)).

## To construct publications
Publications are synced from my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/sSuEkJWCTZOuBEciWPiNuw). With `$ADS_API_TOKEN` set (or the token in `bibliography/SECRET_BIBTEX`), run

```bash
conda run -n cv-ads python bibliography/sync_ads.py
```

This rewrites `content/publication/*/index.md` and `cite.bib` (keeping slugs, `featured.png`, tags, and other hand-set fields), writes `bibliography/publications_ads.bib`, and lists any folders with no matching ADS record. Featured papers are set by `FEATURED` in the script; papers not on ADS are hand-written folders listed in `MANUAL`.

## Docs and references
- [Template repository](https://github.com/HugoBlox/theme-academic-cv)
- [HugoBlox documentation](https://docs.hugoblox.com/)
- [Hugo documentation](https://gohugo.io/documentation/)
