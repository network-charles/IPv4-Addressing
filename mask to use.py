import netaddr
from netaddr import *
import sys

# Write the IP address you will like to subnet
ip = IPNetwork('172.21.1.1/16')
print('This is the IP address you inputted: ' + str(ip))
# show the user the network address of the typed IP address
print('This is the network address of the IP address ' + str(ip.network) + '\n')
# confirm that the prefix length of the network address is correct
ip_prefix = ip.prefixlen

# This is the Network adress
net = str(ip.network)

# Prompt the user up to 3 times before breaking the loop
for i in range(3):
    try:
        # Asks the user a question
        subnet = int(input('How many subnets do you want?\n'))
    except ValueError:
        print('You have not inputted a number')
        # If user does't enter a value, exit the code
        sys.exit()
    else:
        try:
            # Asks the user a question
            host = int(input('How many hosts do you want?\n'))
        except ValueError:
            print('You have not inputted a number')
        else:
            break


print(f'''You are designing a subnet mask for the {net} network. You want ''' + str(subnet) + 
''' subnets with up to ''' + str(host) + ' hosts on each subnets. Which subnet mask should you use?\n''')

# Function call to determine the amount of hosts that contain
def host_that_can_contain():
    global host
    magic_numbers = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - host)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    closest_value = (min(magic_numbers, key=x) * 2) - 2
    print('The amount of hosts that can contain ' + str(host) + ' hosts is:')
    print(str(closest_value) + ' hosts\n')


# Function call to determine the amount of subnet that contain
def subnets_that_can_contain():
    global subnet

    magic_numbers = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

    # Take any value(magic_numbers) passed to you, then, produce an absolute value of it. (This is a function)
    x = lambda magic_number_value: abs(magic_number_value - subnet)

    # Take the list of values then pass it to the lambda function, an absolute value operation will be performed on it.
    # Then each absolute value result from the list will be compared among themselves, the minimum will be selected.
    closest_value = min(magic_numbers, key=x) * 2

    # call the function for host that can contain
    host_that_can_contain()

    print('The amount of subnets that can contain ' + str(subnet) + ' subnets is:')
    # print the amount of subnets thta can contain
    print(str(closest_value) + ' subnets\n')
    
    binary_of_the_closest_value = (closest_value.bit_length() - 1)
    
    # concatenate the network address with prefix length of the new mask to use
    mask_of_the_closest_value = IPNetwork(net + '/' + str(ip_prefix + binary_of_the_closest_value))
    
    # print the new network address and prefix length
    print('The new prefix length of the network address is: ' + str(mask_of_the_closest_value))
    
    # print the new subnet mask to use
    string_of_mask = mask_of_the_closest_value
    print('The mask to use is: ' + str(string_of_mask.netmask))
    print()

# call the function for subnet that can contain
subnets_that_can_contain()
