# 4.1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('FastEthernet', 'GigabitEthernet')

# 4.2
mac = 'AAAA:BBBB:CCCC'
one, two, three = mac.split(':')
ans = '.'.join([one, two, three])

# 4.3
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
ans = config.split()[-1].split(',')

# 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
set_vlans = set(vlans)
ans = sorted(set_vlans)

# 4.5
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
num_cm1 = command1.split()[-1].split(',')
num_cm2 = command2.split()[-1].split(',')
ans = sorted(set(num_cm1) & set(num_cm2))

# 4.6
ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
list_route = ospf_route.split()
ans = "Protocol: {}\nPrefix: {}\nAD/Metric: {}\nNext-Hop: {}\nLast update: {}\nOutbound Interface: {}"\
      .format(list_route[0], list_route[1], list_route[2].strip('[]'), list_route[4], list_route[5], list_route[6])

# 4.7
mac = 'AAAA:BBBB:CCCC'
mac_list = mac.split(':')
one = str(bin(int(mac_list[0], 16)))
two = str(bin(int(mac_list[1], 16)))
three = str(bin(int(mac_list[2], 16)))
ans = one[2:] + two[2:] + three[2:]

# 4.8
ip = '192.168.3.1'
num_ip = ip.split('.')
ans = '{0:<10} {1:<10} {2:<10}\n{0:010b} {1:010b} {2:010b}'.format(int(num_ip[0]), int(num_ip[1]), int(num_ip[2]))
