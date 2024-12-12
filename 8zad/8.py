from itertools import *
#14413
# c = 0
# for s in set(permutations("СОРТИРОВКА")): #пермутатионс это только перестановка букв
#     q = "".join(s)
#     q = q.replace("С", "0")
#     q = q.replace("Р", "0")
#     q = q.replace("Т", "0")
#     q = q.replace("В", "0")
#     q = q.replace("К", "0")
#     q = q.replace("О", "1")
#     q = q.replace("И", "1")
#     q = q.replace("А", "1")
#     if "000" not in q and "111" not in q:
#         c+= 1
# print(c)

#18133
# c=0
# for s in product("ДИКМО", repeat=5):
#     c+= 1
#     q = "".join(s)
#     if q.count("М") == 2 and "ММ" not in q:
#         print(c)