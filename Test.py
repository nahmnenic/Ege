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