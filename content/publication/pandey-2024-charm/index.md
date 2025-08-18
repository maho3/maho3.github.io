---
title: 'CHARM: Creating Halos with Auto-Regressive Multi-stage networks'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Shivam Pandey
- Chirag Modi
- Benjamin D. Wandelt
- Deaglan J. Bartlett
- Adrian E. Bayer
- Greg L. Bryan
- Matthew Ho
- Guilhem Lavaux
- T. Lucas Makinen
- Francisco Villaescusa-Navarro

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-09-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.817983Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*arXiv e-prints*'
publication_short: ''

doi: 10.48550/arXiv.2409.09124

abstract: To maximize the amount of information extracted from cosmological datasets,
  simulations that accurately represent these observations are necessary. However,
  traditional simulations that evolve particles under gravity by estimating particle-particle
  interactions (N-body simulations) are computationally expensive and prohibitive
  to scale to the large volumes and resolutions necessary for the upcoming datasets.
  Moreover, modeling the distribution of galaxies typically involves identifying virialized
  dark matter halos, which is also a time- and memory-consuming process for large
  N-body simulations, further exacerbating the computational cost. In this study,
  we introduce CHARM, a novel method for creating mock halo catalogs by matching the
  spatial, mass, and velocity statistics of halos directly from the large-scale distribution
  of the dark matter density field. We develop multi-stage neural spline flow-based
  networks to learn this mapping at redshift z=0.5 directly with computationally cheaper
  low-resolution particle mesh simulations instead of relying on the high-resolution
  N-body simulations. We show that the mock halo catalogs and painted galaxy catalogs
  have the same statistical properties as obtained from $N$-body simulations in both
  real space and redshift space. Finally, we use these mock catalogs for cosmological
  inference using redshift-space galaxy power spectrum, bispectrum, and wavelet-based
  statistics using simulation-based inference, performing the first inference with
  accelerated forward model simulations and finding unbiased cosmological constraints
  with well-calibrated posteriors. The code was developed as part of the Simons Collaboration
  on Learning the Universe and is publicly available at r̆lhttps://github.com/shivampcosmo/CHARM.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Astrophysics - Cosmology and Nongalactic Astrophysics
- Astrophysics - Astrophysics of Galaxies
- Statistics - Machine Learning

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: arXiv
  url: https://arxiv.org/abs/2409.09124
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
