import netaddr
from netaddr import *
import sys

# Write the IP address and prefix you will like to subnet
ip = IPNetwork('10.0.0.0/8') 

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
        host = int(input('How many hosts do you want?\n'))
    except ValueError:
        print('You have not inputted a number')
        # If user does't enter a value, exit the code
        sys.exit()
    else:
        try:
            # Asks the user a question
            subnet = int(input('How many subnets do you want?\n'))
        except ValueError:
            print('You have not inputted a number')
        else:
            break


print(f'''You are designing a subnet mask for the {net} network. You want ''' + str(subnet) + 
''' subnets with up to ''' + str(host) + ' hosts on each subnets. Which subnet mask should you use?\n''')

# Function call to determine the amount of hosts that contain
def host_that_can_contain():
    global host
    magic_numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    
    # compare the inputed host value to the magic_number list
    if host in range(0, 2):
        amount_of_host_that_can_contain = magic_numbers[0]
    elif host in range(2, 4):
        amount_of_host_that_can_contain = magic_numbers[1]
    elif host in range(4, 8):
        amount_of_host_that_can_contain = magic_numbers[2]
    elif host in range(8, 16):
        amount_of_host_that_can_contain = magic_numbers[3]
    elif host in range(16, 32):
        amount_of_host_that_can_contain = magic_numbers[4]
    elif host in range(32, 64):
        amount_of_host_that_can_contain = magic_numbers[5]
    elif host in range(64, 128):
        amount_of_host_that_can_contain = magic_numbers[6]
    elif host in range(128, 256):
        amount_of_host_that_can_contain = magic_numbers[7]
    elif host in range(256, 512):
        amount_of_host_that_can_contain = magic_numbers[8]
    elif host in range(512, 1024):
        amount_of_host_that_can_contain = magic_numbers[9]
    elif host in range(1024, 2048):
        amount_of_host_that_can_contain = magic_numbers[10]
    elif host in range(2048, 4096):
        amount_of_host_that_can_contain = magic_numbers[11]
    elif host in range(4096, 8192):
        amount_of_host_that_can_contain = magic_numbers[12]
    elif host in range(8192, 16384):
        amount_of_host_that_can_contain = magic_numbers[13]

    print('The amount of hosts that can contain ' + str(host) + ' hosts is:')
    print(str(amount_of_host_that_can_contain) + ' hosts\n')


# Function call to determine the amount of subnet that contain
def subnets_that_can_contain():
    global subnet

    magic_numbers = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

    # call the function for host that can contain
    host_that_can_contain()

    if subnet in range(0, 2):
        amount_of_subnet_that_can_contain = magic_numbers[0]
    elif subnet in range(2, 4):
        amount_of_subnet_that_can_contain = magic_numbers[1]
    elif subnet in range(4, 8):
        amount_of_subnet_that_can_contain = magic_numbers[2]
    elif subnet in range(8, 16):
        amount_of_subnet_that_can_contain = magic_numbers[3]
    elif subnet in range(16, 32):
        amount_of_subnet_that_can_contain = magic_numbers[4]
    elif subnet in range(32, 64):
        amount_of_subnet_that_can_contain = magic_numbers[5]
    elif subnet in range(64, 128):
        amount_of_subnet_that_can_contain = magic_numbers[6]
    elif subnet in range(128, 256):
        amount_of_subnet_that_can_contain = magic_numbers[7]
    elif subnet in range(256, 512):
        amount_of_subnet_that_can_contain = magic_numbers[8]
    elif subnet in range(512, 1024):
        amount_of_subnet_that_can_contain = magic_numbers[9]
    elif subnet in range(1024, 2048):
        amount_of_subnet_that_can_contain = magic_numbers[10]
    elif subnet in range(2048, 4096):
        amount_of_subnet_that_can_contain = magic_numbers[11]
    elif subnet in range(4096, 8192):
        amount_of_subnet_that_can_contain = magic_numbers[12]
    elif subnet in range(8192, 16384):
        amount_of_subnet_that_can_contain = magic_numbers[13]


    print('The amount of subnets that can contain ' + str(subnet) + ' subnets is:')
    # print the amount of subnets that can contain
    print(str(amount_of_subnet_that_can_contain) + ' subnets\n')
    
    binary_of_the_amount_of_subnet_that_can_contain = (amount_of_subnet_that_can_contain.bit_length() - 1)
    
    # concatenate the network address with prefix length of the new mask to use
    mask_of_the_amount_of_subnet_that_can_contain = IPNetwork(net + '/' + str(ip_prefix + binary_of_the_amount_of_subnet_that_can_contain))
    
    # print the new network address and prefix length
    print('The new prefix length of the network address is: ' + str(mask_of_the_amount_of_subnet_that_can_contain))
    
    # print the new subnet mask to use
    string_of_mask = mask_of_the_amount_of_subnet_that_can_contain
    print('The mask to use is: ' + str(string_of_mask.netmask))
    print()

# call the function for subnets that can contain
subnets_that_can_contain()