# P129 — exact piecewise ML success on coupled dephasing line (2026-11-01)

## Scope
Same five-qubit stabilizer code, ideal independent I/Z site errors with p1=p2=t, p3=p4=p5=2t, 0<=t<=1/2. Continuation of P127/P128 in same manuscript.

## Recomputed exact results
Independent Python/SymPy enumeration of all 32 I/Z errors and 16 syndromes verified total probability 1, exactly two supported cosets per syndrome, and 13 interior syndrome winner switches at four distinct thresholds:
a=0.08525822952075639 (root of 16t^3-28t^2+14t-1);
b=1/4;
c=0.31377205775147154 (root of -16t^5+28t^4-38t^3+25t^2-8t+1);
d=0.3709720637607636 (root of 4t^3-5t^2+4t-1).
Root values are approximate displays of exact isolated algebraic numbers.

Piecewise P_ML(t):
[0,a]: -(2t-1)(24t^4-30t^3+4t^2+2t+1)
[a,b]: -(t-1)(32t^4-24t^3+t+1)
[b,c]: (t-1)(32t^4-24t^3+t-1)
[c,d]: 2t(24t^4-42t^3+31t^2-12t+3)
[d,1/2]: -4t^2(4t-3).

All region formulas obtained from exact syndrome-wise max identities. At each midpoint, independently evaluated sum of per-syndrome maxima agrees with polynomial branch. Exact polynomial identities and root isolation used; numerical decimals only for display. Endpoint ties do not alter success value. The nominal fixed decoder selected at homogeneous t=u=0.1 has P_D(t)=-(2t-1)(24t^4-30t^3+4t^2+2t+1), not equal to P_ML beyond first switch.

## Limitations
This is an instance-specific exact characterization, not proof of novel general method. The independent enumeration uses same model but not a separately developed codebase or published competing implementation. No claims of matched benchmark or Q1 readiness. Local reproducibility script available as conversation artifact p129.py. Next: test endpoint/minimax claims and genuine prior-art novelty.
