import ipaddress
import random

# Signifies the octets in the IP address
octect1 = random.randint(1, 255)
octect2 = random.randint(1, 255)
octect3 = random.randint(1, 255)
octect4 = random.randint(1, 255)
mask = random.randint(8, 31)

# Combine all the octets to become an IP address
ip = f'{octect1}.{octect2}.{octect3}.{octect4}/{mask}'

# Asks the user a question
net = str(ipaddress.IPv4Network(ip, strict=False).network_address)
sub = int(input('How many subnets do you want?\n'))
ho = int(input('How many hosts do you want?\n'))
print(f'You are designing a subnet mask for the {net} network. You want ' + str(sub) + ' subnets with up to ' + str(ho) + ' hosts on each subnets.'
        ' Which subnet mask should you use?')
    
def subnets():
    global sub

    magic_numbers = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - sub)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    closest_value = min(magic_numbers, key=x) * 2
    print(str(closest_value) + ' subnets')
    #interesting_octets = [128, 192, 224, 240, 248, 252, 254, 255]

subnets()


def host():
    global ho
    magic_numbers = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - ho)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    interesting_octets = (min(magic_numbers, key=x) * 2) - 2
    print(str(interesting_octets) + ' hosts')
    #interesting_octets = [128, 192, 224, 240, 248, 252, 254, 255]
    

    if interesting_octets == 2:
        print('1 bits')

    if interesting_octets == 4:
        print('2 bits')

    if interesting_octets == 8:
        print('4 bits')

    if interesting_octets == 16:
        print('5 bits')

    if interesting_octets == 32:
        print('6 bits')

    if interesting_octets == 64:
        print('7 bits')

    if interesting_octets == 128:
        print('8 bits')
    
    
    if interesting_octets == 256:
        print('9 bits')
    
    if interesting_octets == 512:
        print('10 bits')

    if interesting_octets == 1024:
        print('11 bits')

    if interesting_octets == 2048:
        print('12 bits')

    if interesting_octets == 4096:
        print('13 bits')

    if interesting_octets == 8190:
        print('14 bits')

    if interesting_octets == 16384:
        print('15 bits')

    if interesting_octets == 32768:
        print('16 bits')
    

    if interesting_octets == 65536:
        print('17 bits')
    
    if interesting_octets == 196608:
        print('18 bits')

    if interesting_octets == 393216:
        print('19 bits')

    if interesting_octets == 786432:
        print('20 bits')

    if interesting_octets == 15723864:
        print('21 bits')

    if interesting_octets == 3145728:
        print('22 bits')

    if interesting_octets == 6291456:
        print('23 bits')

    if interesting_octets == 12582912:
        print('24 bits')


host()