#18266
# for A in range(1000):
#     flag = True
#     for x in range(10000):
#         if ((x&57 == 0) or ((x&23 == 0) <= (not(x&A == 0)))) == 0:
#             flag = False
#             break
#     if flag == True:
#         print(A)
#         break

# 13854
# def Del(x, y):
#     if x % y == 0: return 1
#     else: return 0
# for A in range(10000):
#     flag = True
#     for x in range(1000):
#         if ((Del(x, 15) and not(Del(x, 10))) <= (A < x + 50)) == 0:
#             flag = False
#             break
#     if flag == True: print(A)