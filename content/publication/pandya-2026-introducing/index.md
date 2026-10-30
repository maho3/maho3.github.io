---
title: "Introducing sapphire: Towards Hybrid Physics-Informed, Data-Driven Modeling of Galaxy Formation"
authors:
- "Viraj Pandya"
- "Greg L. Bryan"
- "T. Lucas Makinen"
- "Austen Gabrielpillai"
- "Christopher Carr"
- "Drummond B. Fielding"
- "Lars Hernquist"
- "Matthew Ho"
- "Kartheik Iyer"
- "Christian Kragh Jespersen"
- "Sophie Koudmani"
- "Marta Laska"
- "Pablo Lemos"
- "Christopher C. Lovell"
- "Lucia A. Perez"
- "William F., Jr. Robinson"
- "Rachel S. Somerville"
- "Tjitske K. Starkenburg"
- "Richard Stiskalek"
- "Bryan Terrazas"
- "G. Mark Voit"
author_notes: []
date: "2026-04-01"
publishDate: "2026-10-30T03:59:41Z"
publication_types:
- article
publication: "*arXiv e-prints*"
publication_short: ''
doi: "10.48550/arXiv.2604.06318"
abstract: "Semi-analytic models (SAMs) have been treating galaxy populations as dynamical systems for $\\gtrsim50$ years, but their evolution equations remain poorly constrained. We introduce sapphire, a modular, automatically differentiable, GPU-accelerated SAM written in JAX. For the first time, we compute exact Jacobian and Hessian matrices of a galaxy formation SAM, using the Pandya et al. (2023) nonlinear differential equation system as an example. These allow efficient, interpretable local and global sensitivity analyses, which reveal that supernova energy loading is the key astrophysical parameter. We use gradient descent and Hamiltonian Monte Carlo (HMC) to perform comprehensive mock parameter recovery tests. These indicate that the $z=0$ stellar-to-halo-mass relation alone does not contain enough information to infer many astrophysical parameters. Using observations of star-forming galaxies from the MaNGA survey and the Behroozi et al. (2019) empirical model as one baseline, we derive multiple posteriors assuming different combinations of data, including $z=0$ interstellar medium gas fractions and metallicities. The inferred physical parameters suggest that galaxies self-regulate their star formation primarily through preventative rather than ejective feedback, though this remains uncertain due to the lack of satellite galaxies, black holes and multi-phase galactic atmosphere physics. Both Fisher and HMC forecasts demonstrate the potential of sapphire to enable precision inference for galaxy formation and cosmology in a hybrid physics-informed, data-driven way, but more work is needed to expand its library of models and methods. We make sapphire publicly available at https://github.com/virajpandya/sapphire."
summary: ''
tags:
- "Astrophysics of Galaxies"
featured: false
url_pdf: "https://arxiv.org/abs/2604.06318"
links:
- name: ADS
  url: "https://ui.adsabs.harvard.edu/abs/2026arXiv260406318P/abstract"
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
---
