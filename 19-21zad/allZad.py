#18268
from math import *
# def f(s1, s2, m):
#     if s1 + s2 <= 72: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s1 - 3, s2, m-1), f(s1, s2 - 3, m-1), f(ceil(s1/2), s2, m-1), f(s1, ceil(s2/2), m-1)]
#     return any(h) if (m - 1) % 2 == 0 else any(h)
# print([s for s in range(23, 1000) if f(50, s, 2)])
# print([s for s in range(23, 1000) if not(f(50, s, 1)) and f(50, s, 3)])
# print([s for s in range(23, 1000) if not(f(50, s, 2)) and f(50, s, 4)])

#18199
# def f(s1, s2, m):
#     if s1 + s2 >= 77: 
#         return m % 2 == 0
#     if m == 0: 
#         return False
#     h = [f(s1+3, s2, m-1), f(s1, s2+3, m-1), f(s1*3, s2, m-1), f(s1, s2*3, m-1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 65) if f(12, s, 2)])
# print([s for s in range(1, 65) if not(f(12, s, 1)) and f(12, s, 3)])
# print([s for s in range(1, 65) if not(f(12, s, 2)) and f(12, s, 4)])

#18144
# def f(s1, m):
#     if s1 <= 19: return m%2 == 0
#     if m == 0: return False
#     h = [f(s1-4, m-1), f(s1-6, m-1), f(ceil(s1/2), m-1)]
#     return any(h) if (m-1) % 2 == 0 else all(h)
#print([s for s in range(20, 100) if f(s, 2)])
# print([s for s in range(20, 100) if f(s, 3) and not(f(s,1)) and not(f(s,2))])
# print([s for s in range(20, 140) if not(f(s,2)) and f(s,4)])

# 13084
# def f(s1, m):
#     if s1 >= 84: return (m%2) == 0
#     if m ==0: return False
#     h = [f(s1+1, m -1)]
#     if s1 % 2 == 0: h.append(f(s1*1.5, m -1))
#     else: h.append(f(s1*2, m -1))
#     return any(h) if (m-1)% 2== 0 else all(h)
# print(max([s for s in range(1, 84) if not(f(s, 1)) and f(s, 2)]))
# print([s for s in range(1, 84) if not(f(s, 1)) and f(s, 3)][:2])
# print(max([s for s in range(1, 84) if not(f(s, 2)) and f(s, 4)]))