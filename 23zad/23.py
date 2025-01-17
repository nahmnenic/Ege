# 19253
# def f(n, m):
#     if n < m or n == 24: return 0
#     if n == m: return 1
#     return f(n - 1, m)+f(n - 6, m)+f(n//2, m)
# print(f(34,29)*f(29,19)*f(19, 6))

# 18936
# def f(n, k):
#     if n > k: return 0
#     if n == k: return 1
#     return f(n+1, k)+f(n+2,k)+f(n*2,k)
# print(f(5,13)*f(13,25))




# 18600
def f(n, k):
    if n > k or n == 30: return 0
    if n == k: return 1
    return f(n+1, k)+f(n*2, k)+f(n*3,k)
print(f(10, 60)*f(60, 70))
# 40+55 = 95





