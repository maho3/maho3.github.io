---
title: Ordered embeddings and intrinsic dimensionalities with information-ordered
  bottlenecks

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Matthew Ho
- Xiaosheng Zhao
- Benjamin D. Wandelt

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-09-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.766176Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Machine Learning: Science and Technology*'
publication_short: ''

doi: 10.1088/2632-2153/ade94d

abstract: We present the information-ordered bottleneck (IOB), a neural layer designed
  to adaptively compress data into latent variables ordered by likelihood maximization.
  Without retraining, IOB nodes can be truncated at any bottleneck width, capturing
  the most crucial information in the first latent variables. Unifying several prior
  approaches, we demonstrate that IOB models achieve efficient compression of essential
  information for a given encoding architecture, while also assigning a semantically
  meaningful ordering to latent representations. IOBs demonstrate a remarkable ability
  to compress embeddings of high-dimensional image and text data, leveraging the performance
  of SOTA architectures such as CNNs, transformers, and diffusion models. Moreover,
  we introduce a novel theory for estimating global intrinsic dimensionality with
  IOBs and show that they recover SOTA dimensionality estimates for complex synthetic
  data. Furthermore, we showcase the utility of these models for exploratory analysis
  through applications on heterogeneous datasets, enabling computer-aided discovery
  of dataset complexity.

# Summary. An optional shortened abstract.
summary: ''

tags:
- neural architectures
- component analysis
- intrinsic dimensionality
- unsupervised learning
- interpretability
- embedding spaces
- adaptive compression

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
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
