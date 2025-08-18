---
title: 'Cosmology with One Galaxy: Autoencoding the Galaxy Properties Manifold'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Amanda Lue
- Shy Genel
- Marc Huertas-Company
- Francisco Villaescusa-Navarro
- Matthew Ho

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-06-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.796602Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*apj*'
publication_short: ''

doi: 10.3847/1538-4357/add724

abstract: Cosmological simulations like CAMELS and IllustrisTNG characterize hundreds
  of thousands of galaxies using various internal properties. Previous studies have
  demonstrated that machine learning can be used to infer the cosmological parameter
  Ω<SUB>m</SUB> from the internal properties of even a single randomly selected simulated
  galaxy. This ability was hypothesized to originate from galaxies occupying a low-dimensional
  manifold within a higher-dimensional galaxy property space, which shifts with variations
  in Ω<SUB>m</SUB>. In this work, we investigate how galaxies occupy the high-dimensional
  galaxy property space, particularly the effect of Ω<SUB>m</SUB> and other cosmological
  and astrophysical parameters on the putative manifold. We achieve this by using
  an autoencoder with an information-ordered bottleneck, a neural layer with adaptive
  compression, to perform dimensionality reduction on individual galaxy properties
  from CAMELS simulations, which are run with various combinations of cosmological
  and astrophysical parameters. We find that for an autoencoder trained on the fiducial
  set of parameters, the reconstruction error increases significantly when the test
  set deviates from fiducial values of Ω<SUB>m</SUB> and A<SUB>SN1</SUB>, indicating
  that these parameters shift galaxies off the fiducial manifold. In contrast, variations
  in other parameters such as σ<SUB>8</SUB> cause negligible error changes, suggesting
  galaxies shift along the manifold. These findings provide direct evidence that the
  ability to infer Ω<SUB>m</SUB> from individual galaxies is tied to the way Ω<SUB>m</SUB>
  shifts the manifold. Physically, this implies that parameters like σ<SUB>8</SUB>
  produce galaxy property changes resembling natural scatter, while parameters like
  Ω<SUB>m</SUB> and A<SUB>SN1</SUB> create unsampled properties, extending beyond
  the natural scatter in the fiducial model.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Galaxy formation
- Hydrodynamical simulations
- Cosmological models
- Cosmological parameters
- '595'
- '767'
- '337'
- '339'
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
  url: https://arxiv.org/abs/2502.17568
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
