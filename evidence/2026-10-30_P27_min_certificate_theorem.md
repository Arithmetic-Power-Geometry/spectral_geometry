# P27 minimal fixed-fibre binomial certificate theorem

Let D=sum_i c_i m_i, where m_i are distinct monomials in one fibre of a monomial substitution, all c_i nonzero rational, sum c_i=0. Allowed certificate terms are lambda(m_i-m_j), lambda rational, with both monomials from this fixed support. Let b be the largest number of disjoint nonempty zero-sum subsets partitioning the coefficient multiset, with indices retained. Then the minimum number of terms is exactly k-b.

Proof: Any certificate determines an edge graph on k supported monomials. Each connected component has zero net coefficient, hence its q components yield a zero-sum partition and q<=b. At least k-q >=k-b edges required. Conversely, take a maximal zero-sum partition and a reference monomial in each block. For every other monomial m_i use c_i(m_i-m_ref); zero-sum forces the correct reference coefficient. This uses sum(|block|-1)=k-b edges. Equality follows.

The proof concerns unrestricted rational coefficients on differences of supported monomials in a fixed fibre; it does NOT establish minimal length using only a predetermined finite generating set of the toric ideal, nor physical genus-two partition functions. For multiple fibres, minimum lengths add under the same allowed-certificate restriction.

Exact subset-DP implementation enumerates zero-sum subsets and recursively maximizes disjoint zero-sum blocks; independently executed on five small test inputs with expected minima 1,2,2,2,3; all PASS. Exponential complexity means no exact P26 756-term global optimum has yet been computed. P26's 613-term construction remains an upper bound, NOT a proved minimum.

Novelty status: not audited against classical zero-sum partitions, network flows, matroid circuits, and toric ideals. No new Q1-level physics theorem established. Manuscript NO-GO.
