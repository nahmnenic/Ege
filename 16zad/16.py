# 607
f = {}
for n in range(30):
    if n == 1:
        f[n] = 3
    if n > 1:
        f[n] = 2*f[n-1] - n + 1
print(f[21])