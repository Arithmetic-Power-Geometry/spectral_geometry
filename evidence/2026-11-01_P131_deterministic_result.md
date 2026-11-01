# P131 exact deterministic minimax result
Model: five-qubit stabilizer, ideal syndrome, independent I/Z site probabilities (t,t,2t,2t,2t), t in [0,1/2].

Exhaustive reduction: at t=1/4, eight syndrome decisions have nonzero mass gaps 1/16 and must be chosen optimally by any decoder with worst-case success above 11/16. The remaining eight tied decisions produce 256 candidates and 21 distinct success polynomials.

Best fixed deterministic success is the global minimum of F(t)=16t^5-28t^4+10t^3+3t^2-2t+1, approximately 0.7495918985924896 at t approximately 0.2633732449103757, a root of F'(t)=2(40t^4-56t^3+15t^2+3t-1). One maximizing choice string over sorted cosets and syndromes 0..15 is 0011011000111011. Each of the other 20 polynomials has an exact rational witness with value below 749591/1000000. The best randomized value is 3/4 from P130, giving strict but small randomization advantage about 0.0004081014.

This is an instance-specific result, not a new general theorem or journal novelty finding. Reproduction and independent checking remain important.