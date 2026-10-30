# P77 — Exact character inversion and hostile novelty audit
Date: 2026-10-30

## Question
Can a full collection of Z2 x Z2 target-translation twined spectra reveal parity-sector multiplicities not visible in ordinary spectra, and is that a new theorem?

## Theorem (classical, not new)
For momentum-parity sector counts N_xy(E,s), x,y in {0,1}, define T_ab(E,s)=sum_xy (-1)^(ax+by) N_xy(E,s). Then N_xy(E,s)=(1/4) sum_ab (-1)^(ax+by) T_ab(E,s), by character orthogonality on Z2 x Z2. Ordinary spectrum is T_00. The complete twining vector is equivalent to parity-sector-resolved data for a *fixed, identified* group action.

## Executed verification
Exact standard-library Python at papers/PAPER-04/code/p77_character_inversion.py. Energy-complete E<=3 using rational coercivity bound for rectangular B=0 models (A,r)=(1,1),(2,3/2),(3/2,2). Four-character forward transform and inverse checked exactly. Results: 18,14,15 populated (E,s,parity) sectors respectively, 28,52,52 Fourier coefficient slots; all PASS. Note parity sectors with zero counts are included in inverse and tested.

## Novelty and physical gates
Fourier inversion is elementary finite abelian harmonic analysis, not new. The translation characters act trivially on oscillators, so the zero-mode trace is a legitimate ingredient of the full twined partition function, but no twisted-sector modular covariance is proved here. For two inequivalent models, one must identify symmetry groups up to conjugacy/automorphism; a fixed coordinate label can create false discrepancies (P76). There is no verified pair of duality-inequivalent fully isospectral theories distinguished by these twined observables.

Strong primary prior art: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011; Ando, Kawabata, Nishioka, Gauging Z_N symmetries of Narain CFTs, JHEP 02 (2026) 058, DOI 10.1007/JHEP02(2026)058. The latter explicitly treats charge symmetries and orbifolds.

## Decision and P78
No new theorem; Paper 4 writing NO-GO. P78 should inspect a literature-certified isospectral, inequivalent graph-code pair and rigorously determine whether an intrinsic, transportable symmetry group/character identification exists. If not, stop twining direction rather than claim spurious novelty. Independently verify any physical theta substitution and twisted-sector modular consistency.
