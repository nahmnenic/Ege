# from math import *
# data = [tuple(map(float, x.split())) for x in open('ФАЙЛ')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 0.8]
#         cl[-1] += n
#         for p in n: data.remove(p)
# РАЗБИЕНИЕ НА КЛАСТЕРЫ


# def plot(cl):
#     m = []
#     for p in cl:
#         k = len([p1 for p1 in cl if dist(p,p1)<=1])
#         m.append(k)
#     return sum(m)/len(m)
# ПЛОТНОСТЬ

# def Savg(cl):
#     s = k = 0
#     for p in cl:
#         for p1 in cl:
#             if p!=p1:
#                 s += dist(p,p1)
#                 k += 1
#     return s/k
# СРЕДНЕЕ РАСТОЯНИЕ КЛАСТЕРА

# def diametr(cl):
#     m = 0
#     for p in cl:
#         for p1 in cl:
#             m = max(m, dist(p,p1))
#     return m
# ДИАМЕТР КЛАСТЕРА

# def kray(cl):
#     maxsumdist = 0
#     final_kray = [] 
#     for kr in cl:
#         sump = sum(dist(point, kr) for point in cl)
#         if sump > maxsumdist:
#             maxsumdist = sump
#             final_kray = kr
#     return final_kray
# КРАЙ КЛАСТЕРА

# def centroid(c):
#     r = []
#     for p in c:
#         r += [(sum(dist(p, p1) for p1 in c), p)]
#     return min(r)[1]
# ЦЕНТР КЛАСТЕРА