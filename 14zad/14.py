# 18122
# def f(number, base): #перевод в сс
#     if number == 0:
#         return '0'
#     digits = [chr(i) for i in range(48, 58)] # + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
#     result = ""

#     while number > 0:
#         remainder = number % base
#         result = digits[remainder] + result
#         number //= base

#     return result

# for x in range(5555):
#     v = 5**150 + 5**135 - x
#     z = f(v, 5)
#     if str(z).count('4') == 134:
#         print(x)

# 17973
# q = []
# alf = [chr(i) for i in range(48,58)]+[chr(i) for i in range(65,91)]
# for x in alf[:24]:
#     v = int(f'12{x}734',24)+int(f'8{x}95{x}3',24)+int(f'24{x}796',24)
#     if v%23 == 0:
#         q.append(v)
# print(max(q)//23)

# 17870
# q = []
# def f(n, b):
#     alf = [chr(i) for i in range(48,58)]
#     res = ''
#     while n > 0:
#         ost = n%b
#         res = alf[ost] + res
#         n//=7
#     return res
# for x in range(2031):
#     v = 7**170 +7**100 - x
#     if f(v, 7).count('0') == 71:
#         q.append(x)
# print(max(q))

#18616
# q = []
# def f(n, b):
#     n = n[::-1]
#     s =0
#     for i in range(len(n)):
#         s += n[i]*b**i
#     return s
        
# alf = [chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
# for x in range(37):
#     v = f([12, 5,9,x,11,10,9,8,15], 37) * f([14,3,x,5,13,10,9,12,6],37)
#     if v % 36==0:
#         q.append(x)

# c = max(q)
# itog = f([2,c,1], 37)
# print(itog)
