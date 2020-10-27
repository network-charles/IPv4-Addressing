import netaddr
from netaddr import *
import sys

# Write the IP address you will like to subnet
ip = IPNetwork('172.21.1.1/16')
print('This is the IP address you inputted: ' + str(ip))
# show the user the network address of the typed IP address
print('This is the network address of the IP address ' + str(ip.network))
# confirm that the prefix length is correct
ip_prefix = ip.prefixlen


net = str(ip.network)

for i in range(3):
    try:
        # Asks the user a question
        sub = int(input('How many subnets do you want?\n'))
    except ValueError:
        print('You have not inputted a number')
        sys.exit()
    else:
        try:
            # Asks the user a question
            ho = int(input('How many hosts do you want?\n'))
        except ValueError:
            print('You have not inputted a number')
        else:
            break

try:
    print(f'''You are designing a subnet mask for the {net} network. You want ' + str(sub) + 
    ' subnets with up to ' + str(ho) + ' hosts on each subnets. Which subnet mask should you use?\n''')
except NameError:
    print('You have not inputted any value')
    sys.exit()
    

def subnets():
    global sub

    magic_numbers = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - sub)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    closest_value = min(magic_numbers, key=x) * 2

    print('The amount of subnets that can contain ' + str(sub) + ' subnets is:')
    # print the amount of subnets thta can contain
    print(str(closest_value) + ' subnets')
    
    binary_of_the_closest_value = (closest_value.bit_length() - 1)
    print('The closest value contains ' + str(binary_of_the_closest_value) + ' binary bits')
    
    mask_of_the_closest_value = IPNetwork(net + '/' + str(ip_prefix + binary_of_the_closest_value))
    string_of_mask = mask_of_the_closest_value
    print('The mask to us is: ' + str(string_of_mask.netmask))
    print()

subnets()


def host():
    global ho
    magic_numbers = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - ho)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    closest_value = (min(magic_numbers, key=x) * 2) - 2
    print('The amount of hosts that can contain ' + str(ho) + ' hosts is:')
    print(str(closest_value) + ' hosts')

host()