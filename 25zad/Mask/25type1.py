from re import *
#18298
#for i in range(0, 10**10+1, 1996):
#    if fullmatch(r'1592[02468]*6[\d]8', str(i)) != None:
#        print(i, i//1996)

#5224
#for i in range(10**5+1):
#    if i**2 < 10**10:
#        if fullmatch(r'4[\d]*1[\d]009', str(i**2)) != None:
#            print(i, i**2)

#7345
#n = -1
#for i in range(0, 10**10, 4546):
#    if fullmatch(r'8[\d]*80[\d]*06', str(i)):
#        n += 1
#        if n % 60 == 0:
#           print(i, i//4546)

def f(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if ((k <= 0) or a == 2) and a != 1 and a != -1:
        return True
    else:
        return False
    
p = 1
for i in range(-1, 10**5 + 1, 2):
    if f(i):
        p += 1
        if f(i) and f(p):
            if fullmatch(r'1[\d]*7[\d]7', str(i)) != None:
                print(i, p)