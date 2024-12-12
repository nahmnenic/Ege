#18192
# def f(n):
#     k = []
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             k.append(i)
#             k.append(n // i)
#     k = sorted(list(set(k)))
#     return k
# vse = []
# for i in range(1000001, 1000030):
#     c = []
#     z = 0
#     q = f(i)
#     for x in q:
#         if f(x) == []:
#             c.append(x)
#             z += 1
#     if z == 3:
#         vse.append(i)
#         if(len(vse)) <= 5:
#             print(vse, max(c))

#18148
def f(n):
    k = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            k.append(i)
            k.append(n//i)
    k = sorted(list(set(k)))
    return k

for i in range(900001, 10000000):
    c = 0
    q = f(i)
    if q != []:
        m = min(q) + max(q)
    else:
        m = 0
    if m%100 == 46:
        c += 1
        if c ==5:
            print(i, m)
    