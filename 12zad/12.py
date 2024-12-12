#18158
# s = []
# for n in range(4, 10000):
#     z = 0
#     q = '4' + n*'1'
#     while '411' in q or '1111' in q:
#         if '411' in q:
#             q = q.replace('411', '14')
#         if '1111' in q:
#             q = q.replace('1111', '1')
#     for i in q:
#        z += int(i)
#     s.append(z)
# print(max(s))

# 18262
# def f(n): # функция для определения целое это число или нет
#     if n%2 == 0: return True
#     if n%2 == 1: return True
#     return False

# for n in range(100):
#     c = 0
#     q = '>' + '0'*17 + '3'*n + '2'*17
#     while '>3' in q or '>2' in q or '>0' in q:
#         if '>3' in q:
#             q = q.replace('>3', '22>')
#         if '>2' in q:
#             q = q.replace('>2', '2>')
#         if '>0' in q:
#             q = q.replace('>0', '3>')
#     q = q.replace('>', '')
#     for i in q:
#         c += int(i)
#     if f(c**0.5):
#         print(c)

#18137
q = '1' * 81
while '111' in q or '88' in q:
    if '88' in q:
        q = q.replace('88', '1111')
    if '111' in q:
        q = q.replace('111', '8')
print(q)