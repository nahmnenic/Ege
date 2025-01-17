from itertools import*
# 18481
# s = '67 567 457 35 234 12 123'.split()
# v = 'AB AC BC BD CE DE DF EG FG'.split()
# print(*range(1,8))
# for p in permutations('ABCDEFG'):
#     if all(str(p.index(b)+1) in s[p.index(a)] for a, b in v):
#         print(*p)
        
# 6254
s = '47 57 45 136 236 457 126'.split()
v = 'FB FG BC GC BD GA AE DE EC'.split()
print(*range(1,8))
c = 0
for p in permutations('ABCDEFG'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a, b in v):
        c+=1
        print(*p)
# BDE
# 1) 527 = 42
# 2) 534 =
# 3) 417 =