from ipaddress import *
# 17972
# c = 0
# net = ip_network('123.222.111.192/255.255.255.248')
# for ip in net:
#     bip = bin(int(ip)).zfill(32)[25:]
#     if bip.count('0') % 3 != 0:
#         c+=1
# print(c)

# 19245
# net = ip_network('218.194.82.148/255.255.255.192', 0)
# print(net[-2])

# 18966
# c = 0
# net = ip_network('5.2.5.0/255.255.0.0', 0)
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('0') % 25 == 0:
#         c+=1
# print(c)

# 18928
# c = 0
# net = ip_network('192.168.248.176/255.255.255.240')
# for ip in net:
#     ip = bin(int(ip))[2:].zfill(32)
#     if ip.count('0') == ip.count('1'):
#         c+=1
# print(c)

# from ipaddress import *
# a = bin(48)[2:].zfill(8) + bin(2)[2:].zfill(8)
# b = bin(48)[2:].zfill(8) + bin(0)[2:].zfill(8)
# print(a)
# print('1'*14 + '00')
# print(b)

# net = ip_network('123.215.104.78/255.255.252.0',0)
# print(net[-2])
p = 1000_000* (1.02)**5
print(p)
