---
title: "Creating halos with autoregressive multistage networks"
authors:
- "Shivam Pandey"
- "Chirag Modi"
- "Benjamin D. Wandelt"
- "Deaglan J. Bartlett"
- "Adrian E. Bayer"
- "Greg L. Bryan"
- "Matthew Ho"
- "Guilhem Lavaux"
- "T. Lucas Makinen"
- "Francisco Villaescusa-Navarro"
author_notes: []
date: "2025-11-01"
publishDate: '2025-08-18T00:01:43.817983Z'
publication_types:
- article-journal
publication: "*Physical Review D*"
publication_short: ''
doi: "10.1103/vlm2-tm6k"
abstract: "To maximize the amount of information extracted from cosmological datasets, simulations that accurately represent these observations are necessary. However, traditional simulations that evolve particles under gravity by estimating particle-particle interactions (<inline-formula><mml:math><mml:mi>N</mml:mi></mml:math></inline-formula>-body simulations) are computationally expensive and prohibitive to scale to the large volumes and resolutions necessary for the upcoming datasets. Moreover, modeling the distribution of galaxies typically involves identifying virialized dark matter halos, which is also a time- and memory-consuming process for large <inline-formula><mml:math><mml:mi>N</mml:mi></mml:math></inline-formula>-body simulations, further exacerbating the computational cost. In this study, we introduce CHARM, a novel method for creating mock halo catalogs by matching the spatial, mass, and velocity statistics of halos directly from the large-scale distribution of the dark matter density field. We develop multistage neural spline flow-based networks to learn this mapping at redshift <inline-formula><mml:math><mml:mi>z</mml:mi><mml:mo>=</mml:mo><mml:mn>0.5</mml:mn></mml:math></inline-formula> directly with computationally cheaper low-resolution particle mesh simulations instead of relying on the high-resolution <inline-formula><mml:math><mml:mi>N</mml:mi></mml:math></inline-formula>-body simulations. We show that the mock halo catalogs and painted galaxy catalogs have the same statistical properties as obtained from <inline-formula><mml:math><mml:mi>N</mml:mi></mml:math></inline-formula>-body simulations in both real space and redshift space. Finally, we use these mock catalogs for cosmological inference using redshift-space galaxy power spectrum, bispectrum, and wavelet-based statistics using simulation-based inference, performing the first inference with accelerated forward model simulations and finding unbiased cosmological constraints with well-calibrated posteriors."
summary: ''
tags:
- Astrophysics - Cosmology and Nongalactic Astrophysics
- Astrophysics - Astrophysics of Galaxies
- Statistics - Machine Learning
featured: false
url_pdf: "https://arxiv.org/abs/2409.09124"
links:
- name: ADS
  url: "https://ui.adsabs.harvard.edu/abs/2025PhRvD.112j3503P/abstract"
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
---
