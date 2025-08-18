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
[Tutorial](https://docs.hugoblox.com/reference/content-types/#publications)

Download bibtex from Google Scholar into `bibliography/publications_scholar.bib`. Convert to ADS bibtex with `publications_ads.bib`. Then, convert to markdown

```bash
academic import ./bibliography/publications_ads.bib content/publication/ --compact
```

## Docs and references
- [Template repository](https://github.com/HugoBlox/theme-academic-cv)
- [HugoBlox documentation](https://docs.hugoblox.com/)
- [Hugo documentation](https://gohugo.io/documentation/)
