# 19890
# f = open('/Users/mihail/Downloads/26.txt')
# n, m = map(int, f.readline().split())
# fi = []
# ost = []
# a = []
# for i in range(n):
#     st = int(f.readline())
#     if 310 <= st <= 320:
#         fi.append(st)
#     else: ost.append(st)
# ost.sort()
# for i in ost:
#     if sum(fi) + i <= m:
#         fi.append(i)
# pe = len(fi)
# fi = fi[:-1]
# ost = ost[::-1]
# for i in ost:
#     if sum(fi) + i <= m:
#         fi.append(i)
# print(len(fi), sum(fi))

# 19727
# f = open('26.txt')

# m,n = map(int, f.readline().split())
# a = []
# bid = [int(f.readline()) for i in range(n)]
# bid.sort()
# for i in bid:
#     if sum(a) + i <= m:
#         a.append(i)
# print(len(a))
# a = a[:-1]
# bid.sort(reverse=True)
# mx = 0
# for i in bid:
#     if sum(a) + i <= m:
#         a.append(i)
#         mx = i
# k = 0
# for i in bid:
#     if i > mx:
#         k+=1
# print(len(a),k)
        
# 19726
# f = open('26.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     start, end = map(int, f.readline().split())
#     a.append([start, end])
# a.sort(key= lambda x: x[1])
# k = 0
# pred = 0
# last = 0
# for start,end in a:
#     if start >= last:
#         k+= 1
#         pred = last
#         last = end
# last = pred
# a.sort(key= lambda x: -x[1])
# for start,end in a:
#     if start >= last:
#         print(k, end)
#         break

# 19725
# from math import ceil
# def g(z):
#     return ceil(z/3)

# f = open('26.txt')
# n = int(f.readline())
# d = []
# for i in range(n):
#     i = f.readline()
#     i = int(i)
#     d.append(i)
# d.sort()
# s1 = [i for i in d if i <= 250]
# d = [i for i in d if i > 250][::-1]
# a = []
# b = []
# c = 0
# for i in d:
#     c+=1
#     if c < 4: 
#         a.append(i) 
#     if c == 4:
#         a.append(g(i))
#         c = 0
# k = 0
# z = 0
# for i in d[::-1]:
#     k+=1
#     if k <= 1916: b.append(g(i))
#     else: b.append(i)
# # print(z) 1916
# print(sum(b) + sum(s1))
# print(sum(a) + sum(s1)) # 4317499

# 19256
# f = open('26.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     a.append(list(map(int, f.readline().split())))
# a.sort(key= lambda x: (x[0], x[1]))
# ide = []
# k = 1
# lastid = lastn = mx = 0
# g = 0
# for i in a:
#     curid = i[0]
#     curn = i[1]
#     if curid != lastid:
#         k = 1
#     if curid == lastid and curn == lastn:
#         k = 1
#     if ((curid == lastid) and ((curn - lastn) == 1)):
#         k+=1
#         mx = max(mx, k)
#         if k == 148:
#             ide.append(curid)
#     else: k = 1
#     lastid = curid
#     lastn = curn
# print(min(ide), mx)