# 5.2
ip, bites = input().split('/')
bites = int(bites)
mask_str = '1' * bites + '0' * (32 - bites)
ip_list = ip.split('.')
ans = '''
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{8}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
'''.format(int(ip_list[0]), int(ip_list[1]), int(ip_list[2]), int(ip_list[3]), \
           int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), \
           int(mask_str[24:32], 2), bites)

# 5.2a
ip, bites = input().split('/')
bites = int(bites)
mask_str = '1' * bites + '0' * (32 - bites)
ip_list = ip.split('.')
ip_list[3] = '0'
ans = '''
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{8}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
'''.format(int(ip_list[0]), int(ip_list[1]), int(ip_list[2]), int(ip_list[3]), \
           int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), \
           int(mask_str[24:32], 2), bites)

# 5.2b
from sys import argv
ip, bites = argv[1].split('/')
bites = int(bites)
mask_str = '1' * bites + '0' * (32 - bites)
ip_list = ip.split('.')
ip_list[3] = '0'
ans = '''
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{8}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
'''.format(int(ip_list[0]), int(ip_list[1]), int(ip_list[2]), int(ip_list[3]), \
           int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), \
           int(mask_str[24:32], 2), bites)


