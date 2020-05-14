trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for intf, vlan in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if vlan[0] == 'add':
            ans = ' {} {} {}'.format(command, vlan[0], (',').join(vlan[1:]))
        elif vlan[0] == 'only':
            ans = ' {} {}'.format(command, (',').join(vlan[1:]))
        else:
            ans = ' {} remove {}'.format(command, (',').join(vlan[1:]))
