# P66 — Hostile novelty kill-test: minimal genus and arithmetic finite determinacy
Date: 2026-10-30

## Prior-art primary sources
1. Johan Henriksson, Ashish Kakkar, Brian McPeak, "Narain CFTs and quantum codes at higher genus", Journal of High Energy Physics 2023, article 011 (April), DOI 10.1007/JHEP04(2023)011. Publisher https://link.springer.com/article/10.1007/JHEP04%282023%29011 . The paper explicitly studies isospectral genus-one theories distinguished at genus two; its §4.4 further notes the rank-16 chiral lattice pair indistinguishable for genus g<=4 but distinguishable at genus 5 (older prior art).
2. Erik Nilsson, Julie Rowlett, Felix Rydell, "The Isospectral Problem for Flat Tori from Three Perspectives", Bulletin of the American Mathematical Society 60 (2023), 39-83, DOI 10.1090/bull/1770, publisher/repository https://research.chalmers.se/en/publication/552274 . It explains theta modular forms and Sturm-type finite coefficient identity certificates for rational integral quadratic forms.
3. Shinichiro Yahagi, "Narain CFTs and error-correcting codes on finite fields", JHEP 08 (2022) 058, DOI 10.1007/JHEP08(2022)058, https://link.springer.com/article/10.1007/JHEP08%282022%29058 .

## Chess-style candidate and strongest reply
C3 broad conjecture: some physically distinct code CFTs agree at low genus and require higher genus. **PRIOR ART KILL**: already known genus-5 rank-16 example, explicitly documented by HKM; genus-2 separation of seven-vertex pair also prior art. Do not relabel as discovery.
Arithmetic fallback: rational quadratic-form theta series can be determined from finitely many coefficients with an appropriate fixed modular-form level/weight, by Sturm bound. **PRIOR ART KILL** of broad finite-determinacy claim. Caution: equality of theta series need not imply lattice isometry; a finite coefficient identity certificate is not an isometry/duality certificate. A bounded-height finite collection is trivially finite, but cannot guarantee identifying different duality classes if full spectra coincide.

## Surviving sharply defined possibilities (unproved)
H1: explicit infinite family of physically inequivalent Narain theories with a provably increasing *minimal separating genus* and exact genus-by-genus physical partition-function identities, beyond rank-16 known example. No evidence yet of existence, unboundedness, or novelty. High risk.
H2: quantitative, computationally feasible certificate of oriented O(d,d;Z) orbit equivalence for bounded-height rational Narain backgrounds using additional spin/symmetry information; must prove full information injectivity on target family and give an explicit complexity bound. Not implied by theta-series Sturm bound. Distinguish duality equivalence from equality of partition functions. High risk.
H3: physically normalized genus-two theta-function separation with certified analytic error and exact modular covariance for a family; HKM provides the partition function structure, so new element must be nontrivial certification or a new family, not the known seven-vertex example.

## Mathematical sanity controls
For any finite set F of models, a finite spectral coefficient cutoff separates all pairs that are distinct in their complete spectra: for each pair choose first differing coefficient and take maximum. This is a finite-set compactness/selection argument and is NOT a new theorem. If two inequivalent models have identical full spectra, no cutoff of those coefficients can distinguish them. Hence a purported finite cutoff identifying duality classes requires a proven injectivity theorem on F or richer observables.

## Decision
C3 broad direction NO-GO as originality claim; arithmetic finite-coefficient determinacy NO-GO as originality claim. H2 is preferred as next tightly falsifiable conjecture because it addresses a physical duality-orbit decision problem rather than merely a theta equality test. H1 remains speculative. No fourth-paper manuscript yet.
## P67 plan
Define a bounded rational moduli domain and oriented O(2,2;Z) action, then test whether the full spin-resolved partition data distinguish orbits on the domain. First seek counterexamples and accidental equalities; if any exist, reject orbit-reconstruction. Do not assume spectral equality implies duality.
