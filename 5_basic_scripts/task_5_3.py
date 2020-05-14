tmpl = {
    'access': [
        'switchport mode access', 'switchport access vlan {}',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
        ],
    'trunk': [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk allowed vlan {}'
    ]
}

# 5.3

r = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
n = input('Введите номер влан(ов): ')

ans = 'interface {}\n'.format(interface) + '\n'.join(tmpl[r]).format(n)

# 5.3a

questions = {
    'access': 'Введите номер VLAN: ',
    'trunk': 'Введите разрешенные VLANы: '
}

r = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
n = input(questions[r])

ans = 'interface {}\n'.format(interface) + '\n'.join(tmpl[r]).format(n)