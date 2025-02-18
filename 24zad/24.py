# 11667 не додумал
# f = open('24.txt').readline()
# l = k = m = 0
# f = f.replace('INFINITY', '1')
# for r in range(len(f)):
#     if f[r] == '1':
#         k += 1
#     while k > 1000:
#         if f[l] == '1':
#             k -= 1
#         l+=1
#     if k == 1000:
#         m = max(m, (r - l + 8 + (k*7)))
# print(m)

# 19254
# f = open('24.txt').readline()
# l = k = m = 0
# for r in range(3, len(f)):
#     if f[r-3: r+1] == 'FSRQ':
#         k+=1
#     while k > 80:
#         if f[l: l+4] == 'FSRQ':
#             k -= 1
#         l+=1
#     if k == 80:
#         m = max(m, r-l+1)
# print(m)

# 18029
# f = open('24.txt').readline().rstrip()
# f = f.split('X')[1:-1]
# k = l = m = 0
# z = []
# c = [0]
# for q in f:
#     m = q.count('Y')
#     if m == 75:
#         z.append(str(len(q)+2) + str(q.count('Y')))
# print(m, z)

# 17756
# f = open('24.txt').readline().rstrip()
# for x in ['++', '+*', '*+', '**']: f = f.replace(x, 'X')
# f = f.split('X')
# z = []
# for s in f:
#     k = len(s)
#     if s[0] != ('+' or '*'):
#         k += 1
#     if s[-1] != ('+' or '*'):
#         k += 1
#     z.append(k)
# print(max(z))

# 16388
# f = open('24.txt').readline().rstrip()
# f = f.replace('KLMN', '4')
# l = k = 0
# a = 'KLMN'
# b = []
# m = []
# for r in range(len(f)):
#     if f[r] == '4':
#         k += 1
#     if f[r] != '4':
#         k = 0
#     b.append(k)
#     if k == 45:
#         m.append(f[r-47: r+5])
# print(max(b)*4, m)

# 7723
# f = open('/Users/mihail/Documents/24_7723.txt').read()
# f = f.replace('8', '1').replace('D', 'R')
# f = f.split('R')
# k = c = 0
# z = []
# for i in f:
#     c+=1
#     if k == 0 and i.count('1') > 2:
#         k+=1
#         z.append(k)
#     elif i.count('1') == 2:
#         k+=1
#         z.append(k)
#     else: k = 0
# print(max(z))

# 7600
# f = open('/Users/mihail/Documents/24_7600.txt').read()
# f = f.replace('Q','1').replace('R','1').replace('S','1')
# f = f.split('11')
# z = []
# for i in f:
#     if i != '':
#         if i[0] == '1':
#             i = i[1:]
#         if i[-1] == '1':
#             i = i[:-1]
#         z.append(len(i)+2) #+2 потому что ['asd', 'qegv'] но между ними 11, и по одной 1 мы можем взять
# print(max(z))

# 8166
# f = open('/Users/mihail/Documents/24_8166.txt').read()
# f = f.replace('A', '1').replace('B', '1').replace('C', '1')
# k = 0
# z = []
# for i in range(len(f)):
#     if f[i] == '1':
#         k+=1
#         z.append(k)
#     else: k = 0
# print(max(z)//2)

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

# 18284
# f = open('/Users/mihail/Downloads/24_18284.txt').readline().strip().replace('L', ' L').split()
# mn = 3000000
# for i in f:
#     o = []
#     v = []
#     e = []
#     if i[0] == 'L':
#         for r in range(len(i)):
#             if i[r] == 'O': o.append(r)
#             if i[r] == 'V': v.append(r)
#             if i[r] == 'E': e.append(r)
            
#             if o != [] and v != [] and e != []:
#                 mnv = [s for s in v if s > min(o)]
#                 mne = [q for q in e if q > min(mnv)]
#                 if mne != []:
#                     mn = min(mn, min(mne)+1)
#                     print(mn)
#  19887
# f = open('/Users/mihail/Downloads/19887.txt').readline().replace('0', 'a').replace('2', 'a').replace('4', 'a').replace('6', 'a').replace('8', 'a')
# f = f.replace('1','b').replace('3','b').replace('5','b').replace('7','b').replace('9','b')
# c = 0
# mx = 0
# for r in range(len(f)-1):
#     cur = f[r]
#     nx = f[r+1]
#     if cur != nx:
#         c+=1
#     else: c = 0
#     mx = max(mx, c+1)
# print(mx)