---
title: Benchmarks and explanations for deep learning estimates of X-ray galaxy cluster
  masses

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Matthew Ho
- John Soltis
- Arya Farahi
- Daisuke Nagai
- August Evrard
- Michelle Ntampaka

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2023-09-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.751729Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*mnras*'
publication_short: ''

doi: 10.1093/mnras/stad2005

abstract: We evaluate the effectiveness of deep learning (DL) models for reconstructing
  the masses of galaxy clusters using X-ray photometry data from next-generation surveys.
  We establish these constraints using a catalogue of realistic mock eROSITA X-ray
  observations which use hydrodynamical simulations to model realistic cluster morphology,
  background emission, telescope response, and active galactic nucleus (AGN) sources.
  Using bolometric X-ray photon maps as input, DL models achieve a predictive mass
  scatter of $σ _łn M_mathrm500c = 17.8~ m̊ per cent$, a factor of two improvements
  on scalar observables such as richness N<SUB>gal</SUB>, 1D velocity dispersion σ<SUB>v,1D</SUB>,
  and photon count N<SUB>phot</SUB> as well as a 32 per cent improvement upon idealized,
  volume-integrated measurements of the bolometric X-ray luminosity L<SUB>X</SUB>.
  We then show that extending this model to handle multichannel X-ray photon maps,
  separated in low, medium, and high energy bands, further reduces the mass scatter
  to 16.2 per cent. We also tested a multimodal DL model incorporating both dynamical
  and X-ray cluster probes and achieved marginal gains at a mass scatter of 15.9 per
  cent. Finally, we conduct a quantitative interpretability study of our DL models
  and find that they greatly down-weight the importance of pixels in the centres of
  clusters and at the location of AGN sources, validating previous claims of DL modelling
  improvements and suggesting practical and theoretical benefits for using DL in X-ray
  mass inference.

# Summary. An optional shortened abstract.
summary: ''

tags:
- 'methods: data analysis'
- 'galaxies: clusters: general'
- 'galaxies: clusters: intracluster medium'
- 'galaxies: nuclei'
- large-scale structure of Universe
- 'X-rays: galaxies: clusters'
- Astrophysics - Cosmology and Nongalactic Astrophysics

# Display this page in a list of Featured pages?
featured: true

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
  url: https://arxiv.org/abs/2303.00005
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
