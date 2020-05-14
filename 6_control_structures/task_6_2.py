# -*- coding: utf-8 -*-

# 6.2
one, two, three, four = input().split('.')
one = int(one)
two = int(two)
three = int(three)
four = int(four)

type = 'Внешний - '
if one == 10 or (one == 172 and 15 < two < 32) or (one == 192 and two == 168):
    type = 'Внутренний - '

if one > 0 and one < 224:
    ans = type + 'unicast'
elif one > 223 and one < 240:
    ans = type + 'multicast'
elif one == two == three == four == 255:
    ans = type + 'local broadcast'
elif one == two == three == four == 0:
    ans = type + 'unassigned'
else: ans = type + 'unused'

# 6.2a

ip = input('Введите IP-адрес: ').split('.')
len = len(ip)
for i in range(len):
    ip[i] = int(ip[i])
    if ip[i] < 0 or ip[i] > 255 or len != 4:
        print('Неправильный IP-адрес')
        break
else:
    type = 'Внешний - '
    if ip[0] == 10 or (ip[0] == 172 and 15 < ip[1] < 32) or (ip[0] == 192 and ip[1] == 168):
        type = 'Внутренний - '

    if ip[0] > 0 and ip[0] < 224:
        ans = type + 'unicast'
    elif ip[0] > 223 and ip[0] < 240:
        ans = type + 'multicast'
    elif ip[0] == ip[1] == ip[2] == ip[3] == 255:
        ans = type + 'local broadcast'
    elif ip[0] == ip[1] == ip[2] == ip[3] == 0:
        ans = type + 'unassigned'
    else: ans = type + 'unused'

# 6.2b

ip = input('Введите IP-адрес: ').split('.')
while True:
    l = len(ip)
    for i in range(l):
        ip[i] = int(ip[i])
        if ip[i] < 0 or ip[i] > 255 or l != 4:
            ans = 'Неправильный IP-адрес'
            break
    else:
        type = 'Внешний - '
        if ip[0] == 10 or (ip[0] == 172 and 15 < ip[1] < 32) or (ip[0] == 192 and ip[1] == 168):
            type = 'Внутренний - '

        if ip[0] > 0 and ip[0] < 224:
            ans = type + 'unicast'
        elif ip[0] > 223 and ip[0] < 240:
            ans = type + 'multicast'
        elif ip[0] == ip[1] == ip[2] == ip[3] == 255:
            ans = type + 'local broadcast'
        elif ip[0] == ip[1] == ip[2] == ip[3] == 0:
            ans = type + 'unassigned'
        else: ans = type + 'unused'
        break
    ip = input('Введите IP-адрес еще раз: ').split('.')
