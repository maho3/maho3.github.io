---
title: Reconstructing Galaxy Cluster Mass Maps using Score-based Generative Modeling

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Alan Hsu
- Matthew Ho
- Joyce Lin
- Carleen Markey
- Michelle Ntampaka
- Hy Trac
- Barnabás Póczos

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.770652Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*The Open Journal of Astrophysics*'
publication_short: ''

doi: 10.33232/001c.142147

abstract: We present a novel approach to reconstruct gas and dark matter projected
  density maps of galaxy clusters using score-based generative modeling. Our diffusion
  model takes in mock SZ and X-ray images as conditional inputs, and generates realizations
  of corresponding gas and dark matter maps by sampling from a learned data posterior.
  We train and validate the performance of our model by using mock data from a hydrodynamical
  cosmological simulation. The model accurately reconstructs both the mean and spread
  of the radial density profiles in the spatial domain, indicating that the model
  is able to distinguish between clusters of different mass sizes. In the spectral
  domain, the model achieves close-to-unity values for the bias and cross-correlation
  coefficients, indicating that the model can accurately probe cluster structures
  on both large and small scales. Our experiments demonstrate the ability of score
  models to learn a strong, nonlinear, and unbiased mapping between input observables
  and fundamental density distributions of galaxy clusters. These diffusion models
  can be further fine-tuned and generalized to not only take in additional observables
  as inputs, but also real observations and predict unknown density distributions
  of galaxy clusters.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Cosmology and Nongalactic Astrophysics
- Machine Learning

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
  url: https://arxiv.org/abs/2410.02857
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
