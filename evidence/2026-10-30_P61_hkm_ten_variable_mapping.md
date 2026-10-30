# P61 — Published genus-two variable map: first reconstruction and falsification

Source: Henriksson, Kakkar, McPeak, *Narain CFTs and quantum codes at higher genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, §3.2.3 eqs. (3.37)-(3.46), primary open access https://scoap3-prod-backend.s3.cern.ch/media/files/76861/10.1007/JHEP04(2023)011_a.pdf.

HKM ten variables (using local labels 1,X,Y,Z):
y0=11; y1=1Y; y2=Y1; y3=YY; y4=1X/1Z; y5=X1/Z1; y6=XX/ZZ; y7=YX/YZ; y8=XY/ZY; y9=XZ/ZX (the last class is the combinatorially consistent completion, requiring confirmation against the actual printed theta expression).

Paper 3 uses a different ten-class rule: (a,b)~(b,a), or exchange of the two copies. Counterexample: HKM identifies 1X and 1Z but distinguishes 1X from X1; copy-exchange identifies 1X with X1, but distinguishes 1X from 1Z. Both quotient sets have ten elements but are not the same quotient. A Python exact combinatorial audit of all 16 ordered pairs passes.

Important: the primary PDF text extraction for equation (3.46) appears to read x[XZ]=x[ZZ], which would contradict y6=x[XX]=x[ZZ] and omit ZX. This may be a typographical error or extraction artifact. DO NOT silently claim the physical theta map is fully established; inspect the original equation visually, verify against theta identities, and compare published implementation if available. Also verify eq (3.48) separating map from original typeset page, not OCR-like text extraction.

Paper 3's algebraic separating factorization of the complete ordered 16-variable polynomial is still plausible independently. Its assertion that its copy-exchange ten-variable polynomial equals the HKM genus-two refinement is unsupported and must be corrected. Prior genus-two coefficient counts and sign certificates cannot be automatically transferred across quotient maps.

Next: P62 verify the exact theta map including y9, reproduce a published reference example, then rerun all affected graph pairs with exact 16-variable enumerators and the verified 10-variable substitution; test separating factorization and modular transformations. Do not claim a new theorem or write Paper 4.
