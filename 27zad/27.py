# 18624
from turtle import *
from math import *

# def visual():
#     up(); tracer(0)
#     for cluster, colour in zip(clusters, ('green', 'red')):
#         for x,y in cluster:
#             goto(x*30, y *30)
#             dot(3, colour)
#     done()

# def centroid(c):
#     r = []
#     for p in c:
#         r += [(sum(dist(p, p1) for p1 in c), p)]
#     return min(r)[1]

# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# clusters = []
# while data:
#     clusters.append([data.pop()])
#     for p1 in clusters[-1]:
#         n = [p for p in data if dist(p1, p) < 2]
#         clusters[-1] += n
#         for p in n: data.remove(p)
# cs = [centroid(cl) for cl in clusters]
# print(int(100000 * sum(p[0] for p in cs) / len(cs)), int(100000 * sum(p[1] for p in cs) / len(cs)))
# visual()

# 20295
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 0.8]
#         cl[-1] += n
#         for p in n: data.remove(p)
        
# def plot(cl):
#     m = []
#     for p in cl:
#         k = len([p1 for p1 in cl if dist(p,p1)<=1])
#         m.append(k)
#     return sum(m)/len(m)

# da = [plot(cl) for cl in cl]

# print(int(min(da)*100_000), int(sum(da)/len(da)*100_000))

# 20206
# def visual(cl):
#     up(); tracer(0)
#     for clu, colour in zip(cl, ('green','blue')):
#         for x,y in clu:
#             goto(x*100, y*100)
#             dot(3, colour)
#     done()
        
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 0.235]
#         cl[-1] += n
#         for p in n: data.remove(p)

# def centr(c):
#     r = []
#     for p in c:
#         r += [(sum(dist(p, p1) for p1 in c), p)]
#     return min(r)[1]

# srarx = sum([centr(x)[0] for x in cl]) / len(cl)
# srary = sum([centr(x)[1] for x in cl]) / len(cl)
# print(int(srarx*10000), int(srary*10000))

# 20205
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# def visual(cl):
#     up(); tracer(0)
#     for clu, colour in zip(cl, ('green', 'blue')):
#         for x, y in clu:
#             goto(x*25, y*25)
#             dot(5, colour)
#     done()
            
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 2]
#         cl[-1] += n
#         for p in n: data.remove(p)

# def cray(clu):
#     mxs = 0
#     r = []
#     for p in clu:
#         k = sum(dist(p, p2) for p2 in clu)
#         mxs = max(mxs, k)
#         if k == mxs:
#             r = p
#     return r
# srarx = (cray(cl[0])[0] + cray(cl[1])[0]) / 2
# srary = (cray(cl[0])[1] + cray(cl[1])[1]) / 2
# print(int(srarx*10000), int(srary*10000))
# print(cray(cl[1])[0])


# 19715
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 5]
#         cl[-1] += n
#         for p in n: data.remove(p)
# cl = [x for x in cl if len(x) > 100]
# def centr(clo):
#     mn = 100000
#     r = []
#     for p1 in clo:
#         summ = 0
#         summ = sum([dist(p1, p) for p in clo])
#         mn = min(mn, summ)
#         if summ == mn: r = p1
#     return r


# srarx = sum([centr(c)[0] for c in cl]) / len(cl)
# srary = sum([centr(c)[1] for c in cl]) / len(cl)
# print(int(srarx*10000), int(srary * 10000)) 
# 132035 86733
# -13054 -128771

# 18678
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# def visual(clo):
#     up();tracer(0)
#     for cl, colour in zip(clo, ('green', 'blue')):
#         for x,y in cl:
#             goto(x*30, y*30)
#             dot(3, colour)
#     done()
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 1]
#         cl[-1] += n
#         for p in n: data.remove(p)
# cl = [x for x in cl if len(x) > 30]
# def centr(cl):
#     mn = 10**20
#     r = []
#     for p1 in cl:
#         summ = sum([dist(p1, p) for p in cl])
#         mn = min(mn, summ)
#         if mn == summ:
#             r = p1
#     return r
# srarx = sum([centr(x)[0] for x in cl]) / len(cl)
# srary = sum([centr(x)[1] for x in cl]) / len(cl)
# print(int(srarx*100_000), int(srary*100_000))
# 346070 215898
# 455364 406022