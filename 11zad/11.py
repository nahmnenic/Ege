# 18614
from math import ceil
def log2(n):
    q = 62 + n
    z = 0
    while q > 1:
        q /=2
        z+=1
    return z

for x in range(100000):
    r = ceil((24 * log2(x))/8) * 5100
    if r <= 174080:
        print(x)