# P92 — Exact two-torus modular-domain duality certificate
Date: 2026-10-30

## Scope and primary source
Hosono, Lian, Oguiso, Yau, c=2 Rational Toroidal Conformal Field Theories via the Gauss Product, Commun. Math. Phys. 241 (2003) 245–286, DOI 10.1007/s00220-003-0927-0, arXiv hep-th/0211230. Appendix C discusses O(2,2;Z), including components; worldsheet parity must be distinguished from orientation-preserving CFT duality. https://arxiv.org/abs/hep-th/0211230

## Exact certificate
G=[[2,1/3],[1/3,3]], det G=53/9, B=±J/3.
tau=(G12+i sqrt(detG))/G11 = 1/6 + i sqrt(53)/6.
rho_plus=1/3+i sqrt(53)/3, rho_minus=-1/3+i sqrt(53)/3.
|tau|²=3/2; |rho±|²=6. All real parts strictly in (-1/2,1/2) and norms >1. Thus each is in the interior of the standard PSL(2,Z) fundamental domain, with unique modular orbit representative. The unordered pair {tau,rho+} differs from {tau,rho-}; its simultaneous reflection {-conj(tau),-conj(rho+)} also differs from {tau,rho-}. This proves inequivalence under PSL(2,Z)^2, exchange and simultaneous reflection. The exact symbolic script asserts these facts.

## Caveat on physical equivalence
Worldsheet parity is often represented as (tau,rho)->(tau,-conj(rho)) and maps rho+ to rho-. Whether worldsheet parity is admitted as an equivalence depends on whether oriented CFT, parity-reflected theory, or unoriented theory is classified. Thus do not claim inequivalence under an equivalence relation that includes worldsheet parity. Spin-resolved partition data distinguish oriented presentations; the parity-reflected spectra have spin reversed. This is a scope-dependent result, not a novel unrestricted Narain counterexample.

## Proof architecture
Einstein-style: formulate transformation-invariant moduli and seek shortest exact certificate. Hawking-style: actively test parity and alternative symmetry explanations. No historical attribution of this particular proof to either physicist.

## Research gate
P92 exact symbolic modular-domain test PASS for specified duality group; parity-scope limitation OPEN; novelty against established two-torus moduli classification NO-GO. P93 should define physically permitted equivalence in paper, then seek a genuinely new precision-limited reconstruction bound, not rebrand this familiar parity example.
