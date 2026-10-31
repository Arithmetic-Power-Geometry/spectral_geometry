"""P108: exact heterogeneous Pauli-channel coupling certificates."""
from fractions import Fraction as F
def epsilon(deltas):
 result=F(1)
 for d in deltas:
  assert 0<=d<=1
  result*=1-d
 return 1-result
GAMMAS={0:F(19096819,10000000000),1:F(2647127,2000000000),28:F(13781397,5000000000)}
if __name__=="__main__":
 for mask,gamma in GAMMAS.items():
  for m in (1,2,5):
   deltas=[F(1,10000)]*m+[F(0)]*(5-m)
   e=epsilon(deltas)
   assert e<=sum(deltas)
   assert 2*e<gamma
   print(mask,m,"epsilon",e,"union",sum(deltas),"certified",True)
 print("PASS exact rational heterogeneous-noise bounds")
