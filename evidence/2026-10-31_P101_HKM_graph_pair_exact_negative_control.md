# P101-QEC — Published seven-vertex pair: independent exact negative control
Date: 2026-10-31
## Provenance
HKM (Henriksson, Kakkar, McPeak), Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, equation (4.19), publisher PDF https://scoap3-prod-backend.s3.cern.ch/media/files/76861/10.1007/JHEP04%282023%29011_a.pdf . Exact matrices transcribed from eq (4.19); publication explicitly reports equal genus-one and different genus-two enumerators. This is established prior art, not our discovery.
## Independently executed test
Python exact bitwise GF(2) implementation, no floating point or external packages. Each graph has 7 independent graph-state generators, 128 stabilizers and k=0 logical qubits.
Both have identical ordinary Pauli support-weight enumerator: {0:1,2:2,3:9,4:17,5:38,6:44,7:17}.
Newly tested coarsened ordered-pair weight-product histogram H(a,b,c)=number of ordered stabilizer pairs (P,Q) with wt(P)=a, wt(Q)=b, wt(PQ)=c. Exhaustively enumerated 128²=16384 pairs per graph. H_A=H_B EXACTLY; zero differing bins. This is a NEGATIVE result; the histogram is NOT the full genus-two complete enumerator and cannot replace it.
## Implication
Simple pairwise support-weight information fails to distinguish this known genus-two-distinguishable pair. This does not show that the full genus-two invariant predicts decoding or logical error correction. A graph state k=0 has no encoded logical qubit; no distance or decoder performance should be claimed.
## Next P102
Construct independently defined [[n,k,d]] codes (k>0) and test actual logical recovery; or seek precise operational interpretation of the complete genus-two invariant. Hostile prior-art audit is mandatory. No paper drafting yet.
