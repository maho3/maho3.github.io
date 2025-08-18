---
title: Sensitivity analysis of simulation-based inference for galaxy clustering

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Chirag Modi
- Shivam Pandey
- Matthew Ho
- ChangHoon Hahn
- Bruno Régaldo-Saint Blancard
- Benjamin Wandelt

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.802194Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*mnras*'
publication_short: ''

doi: 10.1093/mnras/stae2473

abstract: 'Simulation-based inference (SBI) is a promising approach to leverage high-fidelity
  cosmological simulations and extract information from the non-Gaussian, non-linear
  scales that cannot be modelled analytically. However, scaling SBI to the next generation
  of cosmological surveys faces the computational challenge of requiring a large number
  of accurate simulations over a wide range of cosmologies, while simultaneously encompassing
  large cosmological volumes at high resolution. This challenge can potentially be
  mitigated by balancing the accuracy and computational cost for different components
  of the forward model while ensuring robust inference. To guide our steps in this,
  we perform a sensitivity analysis of SBI for galaxy clustering on various components
  of the cosmological simulations: gravity model, halo finder, and the galaxy-halo
  distribution models (halo-occupation distribution, HOD). We infer the <inline-formula><tex-math
  id=\"TM0001\" notation=\"LaTeX\">$σ _8$</tex-math></inline-formula> and <inline-formula><tex-math
  id=\"TM0002\" notation=\"LaTeX\">$Ømega _mathrm m$</tex-math></inline-formula> using
  galaxy power spectrum multipoles and the bispectrum monopole assuming a galaxy number
  density expected from the luminous red galaxies observed using the Dark Energy Spectroscopy
  Instrument. We find that SBI is insensitive to changing gravity model between N-body
  simulations and particle mesh simulations. However, changing the halo finder from
  friends of friends to Rockstar can lead to biased estimate of <inline-formula><tex-math
  id=\"TM0004\" notation=\"LaTeX\">$σ _8$</tex-math></inline-formula> based on the
  bispectrum. For galaxy models, training SBI on more complex HOD leads to consistent
  inference for less complex HOD models, but SBI trained on simpler HOD models fails
  when applied to analyse data from a more complex HOD model. Based on our results,
  we discuss the outlook on cosmological simulations with a focus on applying SBI
  approaches to future galaxy surveys.'

# Summary. An optional shortened abstract.
summary: ''

tags:
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
  url: https://arxiv.org/abs/2309.15071
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
