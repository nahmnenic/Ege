# f = open('qq.txt')
# numbers = list(map(int, f))

# k = 0
# minx = []
# maxsum = -1000000
# for num in numbers:
#     if num > 0 and num % 41 == 0:
#         minx.append(num)
# q = min(minx)

# for i in range(len(numbers) - 1):
#     current = numbers[i]
#     next_item = numbers[i + 1]
    
#     if q % 41 == 0:
#         if current != next_item:
#             if abs(current - next_item) % q == 0:
#                 k += 1
#                 maxsum = max(maxsum, (current + next_item))
# print(k, maxsum)

# 6059
# f = open('17.txt')
# def u(n):
#     z = []
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             if n//i > 100:
#                 z.append(n//i)
#     k = sorted(set(z))
#     return k

# num = list(map(int, f))
# r = []
# c = 0
# for i in range(len(num)-1):
#     nod = []
#     if num[i]%2==0 and num[i+1]%2 ==0:
#         if u(num[i]) != [] and u(num[i]) != []:
#             for d in u(num[i]):
#                 nod.append(d)
#             for p in u(num[i+1]):
#                 nod.append(p)
#             if len(nod) > len(set(nod)):
#                 c += 1
#                 r.append(abs(num[i]-num[i+1]))
# print(c, max(r))