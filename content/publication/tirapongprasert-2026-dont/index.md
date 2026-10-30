---
title: "Don't Cut Corners: How Training Outside the Prior Makes Simulation-Based Inference More Robust"
authors:
- "Chaipat Tirapongprasert"
- "Matthew Ho"
author_notes: []
date: "2026-08-01"
publishDate: "2026-10-30T03:59:41Z"
publication_types:
- article
publication: "*arXiv e-prints*"
publication_short: ''
doi: "10.48550/arXiv.2608.12470"
abstract: "Large astrophysical simulation campaigns often generate training data by sampling parameters across a Uniform prior box. Due to the proposal's sharp edge, neural posterior estimators struggle to learn accurate approximations near the boundaries. We propose Tailed-Uniform, a family of hybrid proposal distributions for sampling training simulations for robust simulation-based inference. By padding the original hard-truncated training box with decaying tails, Tailed-Uniform-trained networks yield more accurate posteriors near and beyond the edges. We demonstrate these improvements on a family of tail shapes, including a widened Uniform box as a control. Our results suggest that additional simulations near the prior boundary better constrain the networks as it approaches the edge of the training box, even for Uniform assumed priors. We show these advantages on a toy problem and cosmological parameter inference from the matter power spectrum. These benefits increase in high dimensions, where boundaries dominate parameter space volume."
summary: ''
tags:
- "Instrumentation and Methods for Astrophysics"
- "Machine Learning"
featured: false
url_pdf: "https://arxiv.org/abs/2608.12470"
links:
- name: ADS
  url: "https://ui.adsabs.harvard.edu/abs/2026arXiv260812470T/abstract"
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
---
