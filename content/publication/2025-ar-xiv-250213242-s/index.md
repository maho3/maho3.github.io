---
title: 'Learning the Universe: $3 h^-1m̊ Gpc$ Tests of a Field Level $N$-body Simulation
  Emulator'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Matthew T. Scoggins
- Matthew Ho
- Francisco Villaescusa-Navarro
- Drew Jamieson
- Ludvig Doeser
- Greg L. Bryan

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-02-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.705480Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*arXiv e-prints*'
publication_short: ''

doi: 10.48550/arXiv.2502.13242

abstract: We apply and test a field-level emulator for non-linear cosmic structure
  formation in a volume matching next-generation surveys. Inferring the cosmological
  parameters and initial conditions from which the particular galaxy distribution
  of our Universe was seeded can be achieved by comparing simulated data to observational
  data. Previous work has focused on building accelerated forward models that efficiently
  mimic these simulations. One of these accelerated forward models uses machine learning
  to apply a non-linear correction to the linear $z=0$ Zeldovich approximation (ZA)
  fields, closely matching the cosmological statistics in the $N$-body simulation.
  This emulator was trained and tested at $(h^-1m̊ Gpc)^3$ volumes, although cosmological
  inference requires significantly larger volumes. We test this emulator at $(3 h^-1
  ̊Gpc)^3$ by comparing emulator outputs to $N$-body simulations for eight unique
  cosmologies. We consider several summary statistics, applied to both the raw particle
  fields and the dark matter (DM) haloes. We find that the power spectrum, bispectrum
  and wavelet statistics of the raw particle fields agree with the $N$-body simulations
  within $∼ 5 %$ at most scales. For the haloes, we find a similar agreement between
  the emulator and the $N$-body for power spectrum and bispectrum, though a comparison
  of the stacked profiles of haloes shows that the emulator has slight errors in the
  positions of particles in the highly non-linear interior of the halo. At these large
  $(3 h^-1rG̊pc)^3$ volumes, the emulator can create $z=0$ particle fields in a thousandth
  of the time required for $N$-body simulations and will be a useful tool for large-scale
  cosmological inference. This is a Learning the Universe publication.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Astrophysics - Cosmology and Nongalactic Astrophysics
- Astrophysics - Astrophysics of Galaxies

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
  url: https://arxiv.org/abs/2502.13242
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
