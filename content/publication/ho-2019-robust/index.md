---
title: A Robust and Efficient Deep Learning Method for Dynamical Mass Measurements
  of Galaxy Clusters

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Matthew Ho
- Markus Michael Rau
- Michelle Ntampaka
- Arya Farahi
- Hy Trac
- Barnabás Póczos

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2019-12-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.732866Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*apj*'
publication_short: ''

doi: 10.3847/1538-4357/ab4f82

abstract: We demonstrate the ability of convolutional neural networks (CNNs) to mitigate
  systematics in the virial scaling relation and produce dynamical mass estimates
  of galaxy clusters with remarkably low bias and scatter. We present two models,
  CNN<SUB>1D</SUB> and CNN<SUB>2D</SUB>, which leverage this deep learning tool to
  infer cluster masses from distributions of member galaxy dynamics. Our first model,
  CNN<SUB>1D</SUB>, infers cluster mass directly from the distribution of member galaxy
  line-of-sight velocities. Our second model, CNN<SUB>2D</SUB>, extends the input
  space of CNN<SUB>1D</SUB> to learn on the joint distribution of galaxy line-of-sight
  velocities and projected radial distances. We train each model as a regression over
  cluster mass using a labeled catalog of realistic mock cluster observations generated
  from the MultiDark simulation and UniverseMachine catalog. We then evaluate the
  performance of each model on an independent set of mock observations selected from
  the same simulated catalog. The CNN models produce cluster mass predictions with
  lognormal residuals of scatter as low as 0.132 dex, greater than a factor of 2 improvement
  over the classical M-σ power-law estimator. Furthermore, the CNN model reduces prediction
  scatter relative to similar machine-learning approaches by up to 17% while executing
  in drastically shorter training and evaluation times (by a factor of 30) and producing
  considerably more robust mass predictions (improving prediction stability under
  variations in galaxy sampling rate by 30%).

# Summary. An optional shortened abstract.
summary: ''

tags:
- 'cosmology: theory'
- 'galaxies: clusters: general'
- 'galaxies: kinematics and dynamics'
- 'methods: statistical'
- Astrophysics - Cosmology and Nongalactic Astrophysics

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
  url: https://arxiv.org/abs/1902.05950
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
