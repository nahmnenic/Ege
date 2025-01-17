alf = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)]
# 9xAB13 + x46C16 - B7x15
for x in alf[:13]:
    a = int(f'9{x}AB', 13) + int(f'{x}46C', 16) - int(f'B7{x}', 15)
    if a % 14 == 0:
        print(x,a//14)