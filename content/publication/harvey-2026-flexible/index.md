---
title: "Flexible simulation-based inference for galaxy photometric fitting with synthesizer"
authors:
- "Thomas Harvey"
- "Christopher C. Lovell"
- "Sophie Newman"
- "Christopher J. Conselice"
- "Duncan Austin"
- "William J. Roper"
- "Aswin P. Vijayan"
- "Stephen M. Wilkins"
- "Patricia Iglesias-Navarro"
- "Vadim Rusakov"
- "Qiong Li"
- "Nathan Adams"
- "Kai Magdwick"
- "Caio M. Goolsby"
- "Marc Huertas-Company"
- "Matthew Ho"
author_notes: []
date: "2026-03-01"
publishDate: "2026-10-30T03:59:41Z"
publication_types:
- article-journal
publication: "*Monthly Notices of the Royal Astronomical Society*"
publication_short: ''
doi: "10.1093/mnras/stag282"
abstract: "We introduce SYNFERENCE, a new flexible Python framework for galaxy spectral energy distribution (SED) fitting using simulation-based inference (SBI). SYNFERENCE leverages the SYNTHESIZER package for flexible forward-modelling of galaxy SEDs and integrates the LTU-ILI package to ensure best practices in model training and validation. In this work we demonstrate SYNFERENCE by training a neural posterior estimator on <inline-formula><tex-math>$10^6$</tex-math></inline-formula> simulated galaxies, based on a flexible eight-parameter physical model, to infer galaxy properties from 14-band Hubble Space Telescope and James Webb Space Telescope (JWST) photometry. We validate this model, demonstrating excellent parameter recovery (e.g. R<inline-formula><tex-math>$^2\\gt $</tex-math></inline-formula>0.99 for M<inline-formula><tex-math>$_\\star$</tex-math></inline-formula>, R<inline-formula><tex-math>$^2\\simeq 0.88$</tex-math></inline-formula> for age) and accurate posterior calibration against nested sampling results. We apply our trained model to 3088 spectroscopically confirmed galaxies in the JWST Advanced Deep Extragalactic Survey GOODS-South field. The amortized inference is exceptionally fast, having nearly fixed cost per posterior evaluation and processing the entire sample in <inline-formula><tex-math>$\\sim$</tex-math></inline-formula>3 min on a single CPU (18 galaxies per CPU per second), a <inline-formula><tex-math>$\\sim 1700\\times$</tex-math></inline-formula> speed-up over traditional nested sampling or Markov Chain Monte Carlo techniques. We demonstrate SYNFERENCE's ability to simultaneously infer photometric redshifts and physical parameters, and highlight its utility for rapid Bayesian model comparison by demonstrating systematic stellar mass differences between two commonly used stellar population synthesis models. SYNFERENCE is a powerful scalable tool poised to maximize the scientific return of next-generation galaxy surveys."
summary: ''
tags:
- "methods: data analysis"
- "techniques: photometric"
- "galaxies: photometry"
- "galaxies: stellar content"
- "Astrophysics of Galaxies"
- "Cosmology and Nongalactic Astrophysics"
- "Instrumentation and Methods for Astrophysics"
featured: false
url_pdf: "https://arxiv.org/abs/2511.10640"
links:
- name: ADS
  url: "https://ui.adsabs.harvard.edu/abs/2026MNRAS.547ag282H/abstract"
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
---
