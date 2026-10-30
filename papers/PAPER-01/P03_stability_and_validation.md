# P03 — Independent exact verification and conditional stability (2026-10-30)

## Execution
The P02 four-probe SymPy algorithm was independently re-executed in a clean Python process using SymPy 1.14.0. Output: PASS exact identities, two rational examples, unrestricted-b negative control. This is independent execution, not a second independent software implementation.

## Explicit elementary stability bound (derived; independent proof audit pending)
Let A=G^-1 have lambda_min(A)>=alpha>0. Let x,y,z,h be the four exact readings from P02 and each noisy reading differ by at most eps in absolute value. Form Ahat from noisy x,y,z as in P02. Each diagonal perturbation is <=eps and off-diagonal perturbation <=3eps/2, so ||Ahat-A||_2 <=||Ahat-A||_F <=sqrt(13/2)eps <3eps.

Assume 3eps<=alpha/2. Then lambda_min(Ahat)>=alpha/2, and with Ghat=Ahat^-1:
||Ghat-G||_2 <= ||A^-1||_2 ||A-Ahat||_2 ||Ahat^-1||_2 <= 6eps/alpha^2.
Let c=G22, chat=Ghat22. Then |chat-c|<=6eps/alpha^2. With b∈[-1/2,1/2], q=(h-c)/x=(1+b)^2∈[1/4,9/4] and x>=alpha, xhat>=alpha/2. Define qhat=(hhat-chat)/xhat. Direct quotient subtraction yields
|qhat-q| <= [ (13/2)/alpha + 12/alpha^3 ] eps = K(alpha) eps.
Indeed |qhat-q| <= (|hhat-h|+|chat-c|)/|xhat| + |h-c| |xhat-x|/(x |xhat|), with |h-c|=x q.
If K(alpha)eps<=1/8 then qhat>=1/8>0 and bhat=sqrt(qhat)-1 is real. Since sqrt(q)>=1/2,
|bhat-b|=|qhat-q|/(sqrt(qhat)+sqrt(q)) <=2 K(alpha) eps.

This is a transparent conservative deterministic bound; not claimed sharp, novel, optimal, or experimentally useful. Its dependence on alpha correctly warns about near-singular A. Note alpha bounds inverse metric, not G itself.

## What this does NOT prove
No minimax lower bound, no noise-optimal probe design, no stability for unlabelled spectra, no global O(2,2;Z)-orbit recovery, and no new CFT equivalence theorem. A four-parameter inverse-function argument is standard.

## P04 research pivot
Rather than publish elementary four-probe inversion and a loose bound, investigate constrained *unlabelled* spectral rigidity under genuinely new hypotheses, or optimal probe design with a sharp minimax condition number. Require independent theorem-level prior-art kill test before choosing a paper.
