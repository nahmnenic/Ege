from re import *
for i in range(0, 10**10, 2024):
    if fullmatch(r'1[\d]*2322[\d]2', str(i)) != None:
        print(i, i//2024)