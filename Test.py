# 20813
# f = open('/Users/mihail/Downloads/24_20813.txt').readline().rstrip().replace('*', '-').replace('--', '- -')
# for q in ('7', '8', '9'): f = f.replace(q, '1')
# f = f.split()
# m = 0
# for i in f:
#     i = i.replace('-01', '-0 ').replace('-00', '-0 0')
#     i = i.split()
#     for d in i:
#         if len(d) > m:
#             d = d.strip('-')
#             m = max(m, len(d))
# print(m)
        
# 20816
# from math import dist
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n=[p for p in data if dist(p1,p) < 2]
#         cl[-1] += n
#         for p in n: data.remove(p)
# # print([len(x) for x in cl])
# def cent(cl):
#     r = []
#     mn = 10**10
#     for p1 in cl:
#         k = sum([dist(p1,p) for p in cl])
#         mn = min(mn, k)
#         if k == mn:
#             r = p1
#     return r
# srarx = sum([cent(x)[0] for x in cl]) / len(cl)
# srary = sum([cent(x)[1] for x in cl]) / len(cl)
# print(abs(srarx)*10000, abs(srary)*10000)

# 20815
# f = open('26.txt')
# n,m = map(int, f.readline().split())
# a = []
# for i in range(n):
#     q = list(map(int, f.readline().split()))
#     q.append(sum(q[1:5]))
#     a.append(q)
# a.sort(key= lambda x: (-x[-1], -x[-2], x[0]))
# q = m
# z = []
# c = 0
# t = 0
# for i in a:
#     if q > 0:
#         z.append([i[-1], i[0]])
#         ze = i[-1]
#         q-=1
#     if i[-1] == ze:
#         z.append([i[-1], i[0]])
# mn = z[-1][0]
# idmn = 0
# for i in z:
#     if i != None:
#         if i[0] == mn +1:
#             idmn = i[-1]
# for i in a:
#     if i[-1] == mn:
#         c+=1
# print(idmn, c)

# 20814
# def f(n):
#     z = []
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             z.append(i)
#             z.append(n//i)
#     z = set(z)
#     return sum(z)
# c = 0
# z = []
# for i in range(500001, 10**10):
#     if str(f(i))[-1] == '9':
#         c+=1
#         if c < 6:
#             print(i, f(i))
#         if c == 5: break

# 17877
# def f(n, k):
#     if n < k: return 0
#     if n == k: return 1
#     return f(n-2, k)+f(n//2, k)
# print(f(38,16)*f(16,2))

# 20811
# def f(s1, m):
#     if s1 >=51: return (m%2) == 0
#     if m == 0: return False
#     h = [f(s1+1, m-1), f(s1+4, m-1), f(s1*2, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print([s for s in range(1, 51) if f(s, 4) and not(f(s,2))])

# 17558
# f = open('17.txt')
# n = list(map(int, f))
# k = 0
# for i in n:
#     if abs(i) % 32 == 0: k+=1
# c = 0
# mx = 0
# for i in range(len(n)-1):
#     cur = n[i]
#     nx = n[i+1]
#     if (cur < 0 or nx < 0) and (cur + nx) < k:
#         c+=1
#         mx = max(mx, cur+nx)
# print(c, mx)

# 17872
# f = {}
# for n in range(1,3000):
#     if n == 1: f[n] = 1
#     else: f[n] = (n-1) * f[n-1]
# print((f[2024] + 2*f[2023])//f[2022])

# 20809
# def Del(n,m): return (n%m)==0
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         f = Del(x,A) or ((60 <= x <= 80) <= (not(Del(x,22))))
#         if f == 0:
#             flag = False
#             break
#     if flag:
#         print(A)

# 20808
# def f(n):
#     alf = '0123456'
#     res = ''
#     while n>0:
#         res = alf[n%7] + res
#         n//=7
#     return res
# mxz = 0
# mxx = 0
# for x in range(1, 2031):
#     v = 7**170 + 7**100 - x
#     mxz = max(mxz, f(v).count('0'))
#     if f(v).count('0') == 73:
#         mxx = max(mxx, x)
# print(mxx)

# 20807
# from ipaddress import *
# net = ip_network('172.16.192.0/255.255.192.0')
# c = 0
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('1') % 5 != 0:
#         c+=1
#         print(c, ip)

# 20806
# s = 81*'1'
# while '111' in s or '88888' in s:
#     if '111' in s: s= s.replace('111', '88',1)
#     else: s = s.replace('88888', '8', 1)
# print(s)

# 20805
# n = 248
# for i in range(100):
#     if n*i*75600 <= 16 * 1024**2 * 8:
#         print(2**i + 1)

# 17863
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     a.sort()
#     p = [x for x in a if a.count(x) !=1]
#     n = [x for x in a if a.count(x) ==1]
#     if len(set(a)) == 4 and len(set(p)) == 1 and len(p) == 3:
#         if (sum(n))**2 < (sum(p))**2:
#             c+=1
#             print(c)

# 17549
# from itertools import*
# c = 0
# for s in product('КОСУФ', repeat=5):
#     c+=1
#     s = ''.join(s)
#     if s.count('У') == 2 and 'Ф' not in s:
#         print(c,s)

# 15319
# from math import log2
# rz = 2764*1793
# i = int(log2(7026)) + 1
# pak = 148
# print((rz*i*pak)//18349566)

# 15318
# from turtle import *
# screensize(4000,4000)
# tracer(0)
# lt(90)
# m = 35
# for i in range(2):
#     fd(13*m)
#     rt(90)
#     fd(18*m)
#     rt(90)
# up()
# fd(5*m)
# rt(90)
# fd(9*m)
# lt(90)
# down()
# for i in range(2):
#     fd(11*m)
#     rt(90)
#     fd(7*m)
#     rt(90)
# up()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*m, y*m)
#         dot(3, 'green')
# done()

# 15317
# mn = 10**10
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n %2 == 0: r += '01'
#     else: r = '1' + r + '1'
#     r = int(r,2)
#     if r > 156: mn = min(mn, n)
# print(mn)

# 15314
# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and not(z)) or (y==z) or not(w)
#                 if f==0:
#                     print(x,y,z,w)
                

# 19257
# from math import dist
# data = [tuple(map(float, x.split())) for x in open('27.txt')]
# cl = []
# while data:
#     cl.append([data.pop()])
#     for p1 in cl[-1]:
#         n = [p for p in data if dist(p1, p) < 2]
#         cl[-1] += n
#         for p in n: data.remove(p)
# # print([len(x) for x in cl])
# def cent(cl):
#     mn = 10**10
#     r = []
#     for p1 in cl:
#         mn = min(mn, sum(dist(p1,p) for p in cl))
#         if mn == sum(dist(p1,p) for p in cl):
#             r = p1
#     return r
# srarx = sum([cent(x)[0] for x in cl]) / len(cl)
# srary = sum([cent(x)[1] for x in cl]) / len(cl)
# print(abs(srarx) * 10000, srary * 10000)

# 19256
# f = open('26.txt')
# n = int(f.readline())
# a = []
# for i in range(n):
#     q = list(map(int, f.readline().split()))
#     a.append(q)
# a.sort(key= lambda x: (x[0], x[1]))
# lastn = 0
# lastz = 0
# ide = []
# mx = 0
# k = 1
# for i in a:
#     if i[0] == lastn and i[1] == lastz+1:
#         k+=1
#         mx = max(mx, k)
#     else:
#         k = 1
#     if k == 148:
#         ide.append(i[0])
#     lastn = i[0]
#     lastz = i[1]
# print(min(ide), mx)

# 19255
# from re import *
# for i in range(0, 10**10, 18579):
#     if fullmatch(r'54[\d]1[\d]3[\d]*7', str(i)) != None:
#         print(i, i//18579)

# 19254
# f = open('/Users/mihail/Downloads/files (1)/24_19.txt').readline().rstrip()
# # f = 'ASFHFSFRSQSKBFSFFRSQJDJD'
# m = l = k = 0
# for r in range(len(f)):
#     if f[r-3:r+1] == 'FSRQ':
#         k +=1
#     while k >= 81:
#         m = max(m, r-l)
#         l+=1
#         if f[l-3:l+1] == 'FSRQ':
#             k-=1
# print(m)

# 19253
# def f(n, k):
#     if n == 24: return 0
#     if n < k: return 0
#     if n == k: return 1
#     return f(n-1,k) + f(n-6,k) + f(n//2, k)
# print(f(34,29)*f(29,19)*f(19,6))

# 19251
# def f(s1, m):
#     if s1 >= 132: return (m%2) == 0
#     if m ==0 : return False
#     h = [f(s1+3, m-1), f(s1+6, m-1), f(s1*3, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print([s for s in range(1, 132) if not(f(s, 2)) and f(s,4)])

# 19249
# f = open('17.txt')
# n = list(map(int, f))
# mx = 0
# for i in n:
#     if len(str(abs(i))) == 5 and abs(i) % 100 == 43 and i > 0:
#         mx = max(mx, i)
# c = 0
# mn = 10**10
# for i in range(len(n)-2):
#     fi = abs(n[i])
#     sc = abs(n[i+1])
#     th = abs(n[i+2])
#     if (fi**2 + sc**2 + th**2) <= mx**2:
#         c+=1
#         mn = min(mn, fi**2 + sc**2 + th**2)
# print(c, mn)
        

# 19248
# f = {}
# for n in range(14000):
#     if n < 5: f[n] = n
#     else: f[n] = 2*n * f[n-4]
# print((f[13766] - 9*f[13762]) //f[13758])

# 19247
# for A in range(1000):
#     flag = True
#     for x in range(1,100):  
#         for y in range(1,100):
#             f = (x- 3*y < A) or (y > 400) or (x > 56)
#             if f == 0:
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break

# 19246
# alf = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)]
# for x in alf[:25]:
#     v = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
#     if v%24 == 0:
#         print(x, v//24)

# 19245
# from ipaddress import *
# net = ip_network('218.194.82.148/255.255.255.192',0)
# for ip in net:
#     print(ip)

# 19244
# def f(s):
#     z = 0
#     for i in s:
#         z+= int(i)
#         if z > 15: return False
#     if z == 15: return True
#     else: return False
# for n in range(4, 10000):
#     s = '1' + n*'2'
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s:
#             s = s.replace('12', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '21', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#     if f(s):
#         print(n)
#         break

# 19243
# sin = 377
# pam = 5536 * 1024 * 8#bit
# for i in range(100000):
#     if i*sin*23155 >= pam:
#         print(i)
#         break

# 19241
# f = open('9.txt')
# c = 0
# for line in f:
#     c+=1
#     a = list(map(int, line.split()))
#     a.sort()
#     n = [x for x in a if a.count(x) == 1]
#     p = [x for x in a if a.count(x) == 3]
#     if len(n) == 1 and len(p) == 6:
#         if n[0] > sum(p)/6:
#             print(c, a)

# 19240
# from itertools import *
# c = 0
# for s in product('АВНРЬЯ', repeat=5):
#     c+=1
#     s = ''.join(s)
#     if s[0] != 'Я' and s.count('Ь') <= 1 and 'ЯЬ' not in s and 'ЬЯ' not in s:
#         print(c, s)

# 19239
# rz = 3840*2160
# i = 24
# pam = 16 * 1024**3 * 8 #bit
# sn = pam // (rz*i)
# vsegokart = 3742//sn + 1
# print(3742 - 5*sn)

# 19238
# from turtle import *
# screensize(4000, 4000)
# tracer(0)
# lt(90)
# m = 30
# for i in range(8):
#     fd(16*m)
#     rt(90)
#     fd(22*m)
#     rt(90)
# up()
# fd(5*m)
# rt(90)
# fd(5*m)
# lt(90)
# down()
# for i in range(8):
#     fd(52*m)
#     rt(90)
#     fd(77*m)
#     rt(90)
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*m,y*m)
#         dot(3, 'green')
# print(17*11)

# 19237
# def f(n):
#     alf = '012'
#     res = ''
#     while n>0:
#         ost = n%3
#         res = alf[ost] + res
#         n//=3
#     return res
# mn = 10**10
# for n in range(1, 225):
#     r = f(n)
#     if n % 3 == 0: r += r[-2:]
#     else: r += f(sum([int(x) for x in r]))
#     r = int(r, 3)
#     if r > 220 and r%2 == 0: 
#         mn = min(mn, r)
# print(mn)

# 19234
# print('y x w z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not((not(x) or y) and not(w)) or not(z and not(y and w))
#                 if f == 0:
#                     print(y,x,w,z)

# 24
# f = open('24.txt').readline()
# alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# gl = [x for x in 'AEIOUY']
# f = f.split('A')
# mx = 0
# for i in f:
#     c = 1
#     a = [alf.index(x) for x in str(i)]
#     if str(i) not in gl:
#         for q in range(len(a)-1):
#             if a[q+1] > a[q]:
#                 c += 1
#                 mx = max(mx, c)
#             else: c = 1
# print(mx)

# яндекс 9
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     if len(set(a)) == 2 or len(set(a)) == 1:
#         c+=1
# print(c)

# яндекс6
# from turtle import *
# screensize(2000, 2000)
# tracer(0)
# m = 50
# left(90)
# rt(60)
# fd(4*m)
# rt(120)
# for i in range(4):
#     fd(3*m)
#     rt(240)
#     fd(3*m)
#     rt(120)
# fd(4*m)
# rt(90)
# fd((8 * (3**0.5)) * m)
# rt(90)
# fd(8*m)
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*m,y*m)
#         dot(3, 'green')
# done()


# 17617
# from re import *
# for i in range(0, 10**10, 8993):
#     if fullmatch(r'89[\d]*4[\d]5[\d]7[\d]', str(i)) != None:
#         print(i, i//8993)

# 17615
# def f(n,k):
#     if n < k: return 0
#     if n == k: return 1
#     return f(n-2, k) + f(n//2, k)
# print(f(32, 8)*f(8, 1))

# 17613
# def f(s1, s2, m):
#     if s1+s2 >= 227: return (m%2) == 0
#     if m == 0: return False
#     h = [f(s1+1,s2,m-1), f(s1,s2+1,m-1), f(s1*2,s2,m-1), f(s1,s2*2,m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print([s for s in range(1, 210) if not(f(17, s, 2)) and f(17, s, 4)])

# 17611
# f = open('17.txt')
# n = list(map(int, f))
# mx = 0
# for g in n:
#     if str(g)[-1] == '7' and len(str(abs(g))) == 4:
#         mx = max(mx, g)
# c = 0
# y = 0
# for i in range(len(n)-2):
#     fi = n[i]
#     sc = n[i+1]
#     th = n[i+2]
#     q = [fi,sc,th]
#     if len(([z for z in q if str(z)[-1] == '7' and len(str(abs(z))) == 4])) >= 2 and sum(q) > mx:
#         c+=1
#         y = max(y, sum(q))
# print(c, y)
    

# 17610
# f = {}
# for n in range(1, 2400):
#     if n == 1: f[n] = 1
#     else: f[n] = (n+1)* f[n-1]
# print((f[2024] + 3*f[2023])//f[2022])
    

# 17609
# def Del(n, m):
#     if n%m == 0: return True
#     else: return False
# mx = 0
# for A in range(1, 10000):
#     flag = True
#     for x in range(1, 1000):
#         if ((Del(x,33)) <= (((not(Del(x, A)))) <= (not(Del(x, 242))))) == False:
#             flag = False
#             break
#     if flag:
#         mx = max(mx, A)
# print(mx)

# 17608
# def f(n):
#     alf = '012345'
#     res = ''
#     while n > 0:
#         ost = n%6
#         res = alf[ost] + res
#         n//=6
#     return res
# mx =0
# for x in range(1,2031):
#     v = 6**2030 + 6**100 - x
#     mx = max(mx, f(v).count('0'))
# print(mx)
    
# 17607
# from ipaddress import *
# net = ip_network('115.198.0.0/255.254.0.0')
# c = 0
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('1') % 5 == 0:
#         c+=1
#         print(c)

# 17606
# s = 81*'9'
# while '33333' in s or '999' in s:
#     if '33333' in s:
#         s = s.replace('33333', '99',1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)

# 17605
# from math import *
# alf = 10 + 2030
# i = int(log2(alf))+1
# c = 318

# for k in range(10000):
#     z = ceil(i*k/8)
#     if c*z >= 67*1024:
#         print(k)
#         break

# 17603
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     a = sorted(a)
#     mna = min(a)
#     mxa = max(a)
#     if len(set(a)) == 4 and (mna + mxa) > (sum(a) - (mna + mxa)):
#         c+=1
#         print(c, a)

# 17602
# from itertools import *
# c = 0
# z = [f for f in 'BCD']
# for s in product('0123456789ABCD', repeat=5):
#     s = ''.join(s)
#     if s.count('9') == 1 and len([x for x in s if x in z]) <= 3 and s[0] != '0':
#         c+=1
# print(c)
        

# 17601
# razmer = 1280*960
# paket = 24

# v = 1392640 #bit
# for i in range(10000):
#     if razmer*paket*i/v <=180:
#         print(2**i)


# 17600
# from turtle import *
# screensize(5000, 5000)
# tracer(0)
# m = 30
# left(90)
# for i in range(2):
#     fd(6*m)
#     right(90)
#     fd(12*m)
#     right(90)
# up()
# fd(1*m)
# right(90)
# fd(3*m)
# left(90)
# down()
# for i in range(2):
#     fd(77*m)
#     right(90)
#     fd(45*m)
#     right(90)
# up()
# for x in range(-10,100):
#     for y in range(-100,100):
#         goto(x*m, y*m)
#         dot(5, 'green')
# done()

# 17599
# mn = 10000000000000
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     z = sum([int(x) for x in r])
#     r += str(z%2)
#     v = sum([int(x) for x in r])
#     r += str(v%2)
#     r = int(r, 2)
#     if r > 123:
#         mn = min(mn, r)
# print(mn)

# 17594
# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((not(x)) and y and z and (not(w))) or ((not(x)) and y and (not(z)) and (not(w))) or (x and y and z and (not(w)))
#                 if f == 1:
#                     print(x,y,z,w)

# 17978
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((w <= y) <= x) or (not(z) and (x <= y))
#                 if f ==0:
#                     print(x,y,z,w)

# 17769
# from re import *
# for i in range(0, 10**10, 2025):
#     if fullmatch(r'21[\d]3[\d]*145[\d]5', str(i)) != None:
#         print(i, i//2025)
    

# 17756
# f = open('/Users/mihail/Downloads/files/24_17756.txt').readline().rstrip()
# f = f.replace('+', 'a').replace('*', 'a')
# f = f.split('aa')
# mx = 0
# for line in f:
#     if line[0] != 'a' and line[-1] != 'a':
#         mx = max(mx, len(line)+2)
#     if line[0] == 'a' and line[-1] != 'a':
#         mx = max(mx, len(line)+1)
#     if line[0] != 'a' and line[-1] == 'a':
#         mx = max(mx, len(line)+1)
#     if line[0] == 'a' and line[-1] == 'a':
#         mx = max(mx, len(line))
# print(mx)

# 17754
# def f(n, k):
#     if n == 22: return 0
#     if n > k: return 0
#     if n == k: return 1
#     return f(n+3, k) + f(n+4, k)
# print(f(16,38))

# 17752
# def f(s1, m):
#     if s1 >= 54: return (m%2) == 0
#     if m == 0: return 0
#     h = [f(s1+2, m-1), f(s1*2, m -1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print([s for s in range(1, 54) if not(f(s, 1)) and f(s,2)])
# print([s for s in range(1, 54) if not(f(s, 1)) and f(s,3)])
# print(min([s for s in range(1, 54) if not(f(s, 2)) and f(s,4)]))

# 17750
# f = open('17.txt')
# n = list(map(int, f))
# c = 0
# mx = 0
# for i in range(len(n) - 1):
#     cu = n[i]
#     nx = n[i+1]
#     if (cu%77 + nx%77) == min(n):
#         c += 1
#         mx = max(mx, cu+nx)
# print(c, mx)

# 17755
# f = {}
# for n in range(1000, 0, -1):
#     if n > 400:
#         f[n] = n**n
#     if n <= 400:
#         f[n] = n+6+f[n+12]
# print(f[72] - f[108])

# 17748
# for A in range(100):
#     flag = True
#     for x in range(100):
#         for y in range(100):
#             if ((x <= 19) or (y < (2*x + A - 50)) or (y > 17)) == False:
#                 flag = False
#                 break
#     if flag == True:
#         print(A)
#         break

# 17768
# n = 4**644 + 4*322 + 16**35 - 64**3
# alf = '0123'
# res = ''
# while n > 0:
#     ost = n%4
#     res = alf[ost] + res
#     n//=4
# print(res.count('3'))

# 17767
# from ipaddress import *
# net = ip_network('228.172.236.0/255.255.240.0', 0)
# c = 0
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('1') % 5 != 0:
#         c+=1
# print(c) 

# 17746
# s = 68 * '9'
# while '22222' in s or '9999' in s:
#     if '22222' in s:
#         s = s.replace('2222', '99', 1)
#     else: s = s.replace('9999', '29', 1)
# print(s.count('9'))

# 17745
# from math import log2
# kod = 256
# alf = 4080+10
# i = 12
# veskoda = 256*12 // 8
# print((veskoda * 2**16) / 1024 / 1024)

# 17770
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     a = sorted(a)
#     mxa2 = a[4]
#     mxa1 = a[3]
#     z = [q for q in a if q%10 == 5]
#     f = [s for s in a if a.index(s) < 3]
#     if (2*(mxa1+mxa2)) > (3*sum(f)):
#         if len(z) >= 2:
#             c+=1
#             print(c, a)

# 17766
# from itertools import *
# c = 0
# for s in product('БЕНРСТЬЯ', repeat=5):
#     c +=1
#     s= ''.join(s)
#     if s[0] == 'Р' and 'Ь' not in s and c%2 == 0:
#         print(c, s)

# 17747
# V = 16000 * 51 * 2 * 1560
# vs = 2**26
# print(V/vs)

# 17774
# from turtle import *
# screensize(5000, 5000)
# tracer(0)
# m = 35
# left(90)
# for i in range(5):
#     forward(8*m)
#     right(90)
#     forward(11*m)
#     right(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*m, y*m)
#         dot(5, 'green')
# done() #12*9 = 108

# 17765
# mn = 100000
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     if r.count('1') % 2 == 0:
#         r += '11'
#     else:
#         r += '01'
#     r = int(r,2)
#     if r > 61:
#         mn = min(mn, r)
# print(mn)

# 17773
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (y <= x) and (not(w)) and z
#                 if f ==1:
#                     print(x, y, w ,z)

# 2503
# f = open('/Users/mihail/Downloads/files (1)/24_2503.txt').read()
# f = f.split()
# c = 0
# for i in f:
#     co = ca = 0
#     for r in range(len(i)):
#         if i[r-1:r+2] == 'AOA':
#             ca += 1
#         if i[r-1:r+2] == 'OAO':
#             co += 1
#     if ca > co:
#         c +=1
# print(c)

# 280
# def f(n):
#     z = []
#     for i in range(10, 100):
#         if n%i == 0 and i != n:
#             z.append(i)
#     z = sorted(set(z))
#     return z
# for i in range(333555, 778000):
#     if len(f(i)) == 35:
#         print(min(f(i)), max(f(i)))

# 4112
# def f(n, k):
#     if n > k: return 0
#     if n == k: return
#     return f(n+2, k) + f(n*2, k)
# print(f(1, 100))

# 5637
# def f(s1, s2, m):
#     if (s1 + s2) >= 245: return (m%2) == 0
#     if m == 0: return False
#     h = [f(s1+1, s2, m-1), f(s1, s2+1, m-1), f(s1*2, s2, m-1), f(s1, s2*2, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print([s for s in range(1, 225) if f(15, s, 2)])

# 4365
# f = open('17.txt')
# n = list(map(int, f))
# mn = 100000
# for i in n:
#     if i%43 == 0:
#         mn = min(mn, i)
# c = mx = 0
# for i in range(len(n)-1):
#     cur = n[i]
#     nx = n[i+1]
#     if (cur + nx) % mn == 0 and not(str(cur)[-1] == str(mn)[-1]) and not(str(nx)[-1] == str(mn)[-1]):
#         c+=1
#         mx = max(mx, cur)
#         mx = max(mx, nx)
#     if (cur + nx) % mn != 0 and (str(cur)[-1] == str(mn)[-1] or str(nx)[-1] == str(mn)[-1]):
#         c+=1
#         mx = max(mx, cur)
#         mx = max(mx, nx)
# print(c, mx)

# 17755
# f = {}
# for n in range(1000, 0, -1):
#     if n > 400:
#         f[n] = n**n
#     else:
#         f[n] = n + 6 + f[n+12]
# print(f[72] - f[108])

# 7353
# def Del(n, m):
#     if n%m ==0: return True
#     else: return False

# c = 0
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         B = 70 <= x <= 80
#         if (Del(x, A) or (B <= (not(Del(x, 18))))) == False:
#             flag = False
#             break
#     if flag == True:
#         c+=1
# print(c)
            
# 247
# def f(n, b):
#     alf = '012345678'
#     res = ''
#     n = int(n)
#     while n > 0:
#         ost = n%b
#         res = alf[ost] + res
#         n//=b
#     return res
# mn = 1010100101010
# for n in range(1, 1000):
#     r = f(n, 8)
#     t = f(n, 9)
#     if r[-1] == '0' and t[-1] == '0':
#         mn = min(mn, n)
# print(mn)

# 17710
# from ipaddress import *
# net = ip_network('214.187.224.0/255.255.224.0')
# c = 0
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('1') % 6 != 0 and ip[28:] == '1000':
#         c +=1
#         print(c, ip)

# 7002
# def f(n):
#     z = 0
#     for i in n:
#         if i != '>':
#             z += int(i)
#     return str(z)  
  
# mn = 10000000  
# for n in range(1000):
#     s = '>' + 40*'0' + n*'1' + 40*'2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     if len(f(s)) == 3 and len(set(f(s))) == 1:
#         mn = min(mn, n)
# print(mn)

# 7997
# ide = 55
# i = 7
# veside = (55*7)//8 + 1
# print(veside*71902 / 1024 / 1024)

# 2041
# f = open('9.txt')
# c = 0
# for line in f:
#     a = list(map(int, line.split()))
#     fi = a[0]
#     se = a[1]
#     th = a[2]
#     fo = a[3]
#     if (fi < se + th + fo) and (se < fi + th + fo):
#         if (th < se + fi + fo) and (fo < fi + th + se):
#             c+=1
# print(c)
 
# 7810
# from itertools import *
# c = 0
# g = 'АО'
# for s in product('МАСЛО', repeat=6):
#     s=''.join(s)
#     z = [x for x in s if x in g]
#     if len(z) == 1:
#         c+=1
#         print(c, s)

# 9362
# rzm = 4 * 1024 * 1024
# print()

# 5871
# from turtle import *
# screensize(5000, 5000)
# tracer(0)
# m = 30
# left(90)
# for i in range(7):
#     forward(20*m)
#     right(240)
#     forward(10*m)
#     right(240)
#     forward(20*m)
#     right(120)
#     forward(10*m)
#     right(120)
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*m, y*m)
#         dot(5, 'green')
# done()

#2348
# q = []
# for n in range(9, 1000):
#     r = n - n%8
#     r = bin(r)[2:]
#     z = sum([int(x) for x in (r)])
#     if z %2 == 0:
#         r += '00'
#     else:
#         r += '01'
#     r = int(r, 2)
#     if r < 353:
#         q.append(n)
# print(max(q))

# 14651
# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((z <= x) == (w <= y) or (x and w))
#                 if f == 0:
#                     print(x,y,z,w)