# P47 independent reproducibility: execute local /mnt/data/p47_full_theta_certified.py
# Mathematical tail: E >= (3/20)||v||_2^2 for |b|<=1/2.
# H(t)=sum_{v in Z^4}exp(-t E(v)).
# Truncation |v|_inf<=K error <=
# 8 (1+sqrt(pi/(t alpha)))^3 exp(-t alpha (K+1)^2)/
# (1-exp(-t alpha (2K+3))), alpha=3/20.
# Bound follows union over four coordinates, each with +/- tails,
# Gaussian sum bound via integral, and ratio test for j>=K+1.
# The bound is uniform for t>=1.
# WARNING: tiny inverse derivative makes the inferred b ill-conditioned.
# A root of the truncated equation is not a validated root of the full equation.
