---
title: 'RTFAST-Spectra: emulation of X-ray reverberation mapping for active galactic
  nuclei'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Benjamin J. Ricketts
- Daniela Huppenkothen
- Matteo Lucchini
- Adam Ingram
- Guglielmo Mastroserio
- Matthew Ho
- Benjamin Wandelt

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-04-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-08-18T00:01:43.823350Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*mnras*'
publication_short: ''

doi: 10.1093/mnras/staf337

abstract: 'Bayesian analysis has begun to be more widely adopted in X-ray spectroscopy,
  but it has largely been constrained to relatively simple physical models due to
  limitations in X-ray modelling software and computation time. As a result, Bayesian
  analysis of numerical models with high physics complexity have remained out of reach.
  This is a challenge, for example when modelling the X-ray emission of accreting
  black hole X-ray binaries, where the slow model computations severely limit explorations
  of parameter space and may bias the inference of astrophysical parameters. Here,
  we present RTFAST-Spectra: a neural network emulator that acts as a drop in replacement
  for the spectral portion of the black hole X-ray reverberation model RTDIST. This
  is the first emulator for the reltrans model suite and the first emulator for a
  state-of-the-art X-ray reflection model incorporating relativistic effects with
  17 physically meaningful model parameters. We use principal component analysis to
  create a light-weight neural network that is able to preserve correlations between
  complex atomic lines and simple continuum, enabling consistent modelling of key
  parameters of scientific interest. We achieve a <inline-formula><tex-math id=\"TM0001\"
  notation=\"LaTeX\">$mathcal O(10^2)$</tex-math></inline-formula> times speed up
  over the original model in the most conservative conditions with <inline-formula><tex-math
  id=\"TM0002\" notation=\"LaTeX\">$mathcal O(1~ m̊ per cent)$</tex-math></inline-formula>
  precision over all 17 free parameters in the original numerical model, taking full
  posterior fits from months to hours. We employ Markov Chain Monte Carlo sampling
  to show how we can better explore the posteriors of model parameters in simulated
  data and discuss the complexities in interpreting the model when fitting real data.'

# Summary. An optional shortened abstract.
summary: ''

tags:
- Astrophysics - High Energy Astrophysical Phenomena
- Astrophysics - Instrumentation and Methods for Astrophysics

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
  url: https://arxiv.org/abs/2412.10131
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
