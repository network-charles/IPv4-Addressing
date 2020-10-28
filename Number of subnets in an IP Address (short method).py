import netaddr
from netaddr import *
import pprint
from pprint import *

# User can enter any IP address they will like to subnet here
ip = IPNetwork('172.24.0.0/16')

# Subnets the IP address with a prefix length value
subnet_ip = ip.subnet(20)

# Passes the list of subnet to a list
list_of_subnet = list(subnet_ip)

# Prints out all possible subnet IDs
pprint(list_of_subnet)

print()

# Prints out how many subnets is in a given IP address
print('There are a total of ', end='')
print(len(list_of_subnet), end='')
print(' subnet IDs.')