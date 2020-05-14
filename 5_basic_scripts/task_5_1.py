# -*- coding: utf-8 -*-

# 5.1
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

name = input('Введите имя устройства: ')
ans = london_co[name]

# 5.1a

name_device = input('Введите имя устройства: ')
name_param = input('Введите имя параметра: ')
ans = london_co[name_device][name_param]

# 5.1b

name_device = input('Введите имя устройства: ')
name_param = input('Введите имя параметра{}: '.format(tuple(london_co[name_device].keys())))
ans = london_co[name_device][name_param]

# 5.1c

name_device = input('Введите имя устройства: ')
name_param = input('Введите имя параметра{}: '.format(tuple(london_co[name_device].keys())))
ans = london_co[name_device].get(name_param, 'Такого параметра нет')

# 5.1d

name_device = input('Введите имя устройства: ')
name_param = input('Введите имя параметра{}: '.format(tuple(london_co[name_device].keys())))
ans = london_co[name_device].get(name_param.lower(), 'Такого параметра нет')
