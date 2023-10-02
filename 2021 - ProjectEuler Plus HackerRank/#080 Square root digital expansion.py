import math
from decimal import *

N = int(input())
P = int(input())
getcontext().prec = P + 5
print(sum(sum(int(d) for d in str(Decimal(x).sqrt())[:P + 1].replace('.', '')) for x in range(2, N + 1) if
          int(round(math.sqrt(x))) ** 2 != x))
