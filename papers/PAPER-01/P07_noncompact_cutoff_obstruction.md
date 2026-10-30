# P07 — No uniform finite spectral cutoff on unrestricted Narain moduli

## Proposition (proved algebraically, novelty unverified)
For every finite H>=0 there exist uncountably many pairwise O(2,2;Z)-inequivalent two-dimensional Narain backgrounds with identical complete unlabelled zero-mode energy multisets restricted to E<=H.

Proof. Let t>H, G=t I_2 and B=b J with J=[[0,1],[-1,0]] and b in (0,1/2). For any (m,n) in Z^2×Z^2,
E_{t,b}(m,n)=||m+bJn||²/t+t||n||².
If n!=0, E>=t>H. If n=0, E=||m||²/t, independent of b. Thus the entire cutoff multiset is identical for all b in the interval, including multiplicities. The group O(2,2;Z) is countable because its elements are integer matrices; any orbit under this group is at most countable. An uncountable one-parameter family cannot lie in one orbit, and indeed represents uncountably many orbits. QED.

The same argument applies to any finite cutoff, and to any finite list of levels below that cutoff. This is a noncompact-moduli statement, not a compact-family impossibility theorem. It does not show that any two members have the same *full* infinite spectrum, and it does not explicitly classify the orbit of the particular pair b=0,1/5.

## Exact test
For t=10, H=4, b=0 and b=1/5, complete charge enumeration finds 129 zero-mode states and 21 distinct energies in both cases, with equal multiplicities. Winding is absent because t>H. Integer momentum range [-7,7] is sufficient because ||m||²<=40. This test confirms the construction but is not needed for the proof.

## Novelty and scope
The argument is an elementary cusp/degeneration obstruction. It may be standard in inverse spectral geometry or lattice theory. Do not call it a new publishable theorem until a strong literature audit verifies originality and significance. In particular, it does not provide a uniform bound on compact reduced moduli, nor an effective cutoff formula there.
