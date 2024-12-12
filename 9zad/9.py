# 15321
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     if max(a) < (sum(a) - max(a)):
#         if (max(a) + min(a)) == (sum(a) - (max(a) + min(a))):
#             c+= 1
# print(c)

# f = open('9.txt')
# c = 0
# for line in f:
#     summ = 0
#     sump = 0
#     a = list(map(int, line.split()))
#     if len(set(a)) == 5:
#         for z in a:
#             if z < 0:
#                 summ += abs(z)
#             else:
#                 sump += z
#         if summ > sump:
#             c+= 1
# print(c)