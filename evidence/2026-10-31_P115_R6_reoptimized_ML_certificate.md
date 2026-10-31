# P115-R6: Exact nominal-decoder optimality under shared dephasing

For the five-qubit [[5,1,3]] stabilizer code with generators XZZXI, IXZZX, XIXZZ, ZXIXZ, consider independent dephasing on each site with tied probability t: pI=1-t, pZ=t. The decoder selected by maximum likelihood at t=1/10 has success P(t)=(1-t)^3(6t^2+3t+1). Exact enumeration gives 16 syndrome-level competitor comparisons. All gaps are nonnegative throughout [0,1/2], establishing that this nominal decoder remains ML there (ties possible at endpoints). Therefore, on [0,1/4], reoptimized ML success equals P(t) and has exact minimum P(1/4)=459/512, because P'(t)=-30t^2(1-t)^2.

Proof of the nontrivial gap factor: q(t)=t^4-2t^3+4t^2-3t+1. Under t=u/(2(1+u)), u>=0, (1+u)^4 q(t)=(5u^4+20u^3+40u^2+40u+16)/16 >0. Other factors have explicit nonnegative signs on [0,1/2]. Reproducible Python/SymPy evidence and full comparison log are in P115_R6_evidence.zip from the research session. The script's final assertions passed; the archive passed integrity verification.

Scope: exact small-code certificate only. No original general theorem or matched published-method runtime benchmark established. Novelty gate remains NO-GO; draft verified methods and results but not submission-ready originality claims.
