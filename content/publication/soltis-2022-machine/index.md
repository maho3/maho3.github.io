---
title: A Machine-learning Approach to Enhancing eROSITA Observations

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- John Soltis
- Michelle Ntampaka
- John F. Wu
- John ZuHone
- August Evrard
- Arya Farahi
- Matthew Ho
- Daisuke Nagai

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2022-11-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.828335Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*apj*'
publication_short: ''

doi: 10.3847/1538-4357/ac9b1b

abstract: The eROSITA X-ray telescope, launched in 2019, is predicted to observe roughly
  100,000 galaxy clusters. Follow-up observations of these clusters from Chandra,
  for example, will be needed to resolve outstanding questions about galaxy cluster
  physics. Deep Chandra cluster observations are expensive, and it is unfeasible to
  follow up every eROSITA cluster, therefore the objects that are chosen for follow-up
  must be chosen with care. To address this, we have developed an algorithm for predicting
  longer-duration, background-free observations, based on mock eROSITA observations.
  We make use of the hydrodynamic cosmological simulation Magneticum, simulate eROSITA
  instrument conditions using SIXTE, and apply a novel convolutional neural network
  to output a deep Chandra-like \"super observation\" of each cluster in our simulation
  sample. Any follow-up merit assessment tool should be designed with a specific use
  case in mind; our model produces observations that accurately and precisely reproduce
  the cluster morphology, which is a critical ingredient for determining a cluster's
  dynamical state and core type. Our model will advance our understanding of galaxy
  clusters by improving follow-up selection, and it demonstrates that image-to-image
  deep learning algorithms are a viable method for simulating realistic follow-up
  observations.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Convolutional neural networks
- Neural networks
- Galaxy clusters
- Observational cosmology
- Astronomical methods
- X-ray astronomy
- X-ray surveys
- Astronomy image processing
- Astronomy data analysis
- '1938'
- '1933'
- '584'
- '1146'
- '1043'
- '1810'
- '1824'
- '2306'
- '1858'
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
  url: https://arxiv.org/abs/2207.14324
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
