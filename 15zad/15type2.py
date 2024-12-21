# 18044
# def f(x):
#     return (not((32 <= x <= 68) or (54 <= x <= 76)) == (not(a1 <= x <= a2)))

# t = []
# d = [y for x in(32, 68, 54, 76) for y in (x, x+0.1, x-0.1)]
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(f(x) for x in d):
#             t.append(a2-a1)
# print(min(t))

# 17871
# def f(x):
#     return ((15 <= x <= 40) <= (((21 <= x <= 63) and not(a1 <= x <= a2)) <= (not(15 <= x <= 40))))

# t = []
# d = [y for x in (15, 40, 21, 63) for y in(x, x+0.1, x-0.1)]
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(f(x) for x in d):
#             t.append(a2-a1)
# print(min(t))








