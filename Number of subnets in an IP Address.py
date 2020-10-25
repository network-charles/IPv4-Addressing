import ipaddress
import random

def subnets():
    # Signifies the octets in the IP address
    octect1 = random.randint(1, 255)
    octect2 = random.randint(1, 255)
    octect3 = random.randint(1, 255)
    octect4 = random.randint(1, 255)
    mask = random.randint(8, 31)

    # Combine all the octets to become an IP address
    ip = f'{octect1}.{octect2}.{octect3}.{octect4}/{mask}'

    # Asks the user a question
    print(f'How many subnets can you get from this IP address {ip}?')
    sub = str(ipaddress.IPv4Network(ip, strict=False).netmask)

    # Asks the user what is the subnet mask
    net_mask = input('What is the Subnet Mask:\n')

    # If users enter a wrong mask, prompt the user to retry
    while net_mask != sub:
        print("\nWrong Subnet Mask!\nTry again!\n")
        net_mask = input("What is the Subnet Mask: ")

    print('The subnet mask is ' + sub + '\n')

    # Defined the print out to avoid repeated typing
    def Uninteresting():
        print('Not an interesting octet')

    # Try this sliced numbers for the first octet
    try:
        if sub[0:3] == str(255):
            Uninteresting()
    
    # If it fails, finally try the remaining sliced numbers for the first octet
    finally:
        if sub[0:1] == str(0):
            Uninteresting()
        elif sub[0:3] != str(255):
            magicNumber1 = 256 - int(sub[0:3])
            TotalSubnets1 = 256 / magicNumber

            print('\nCongrats! The total subnets are ' + str(TotalSubnets1) + '\n')
   
    # Try this sliced numbers for the second octet
    try:
        if sub[4:7] == str(255):
            Uninteresting()
    
    # If it fails, finally try the remaining sliced numbers for the second octet
    finally:
        if sub[4:5] == str(0):
            Uninteresting()

        elif sub[2:3] == str(0):
            Uninteresting()

        elif sub[4:7] != str(255):
            magicNumber2 = 256 - int(sub[4:7])
            TotalSubnets2 = 256 / magicNumber2
            
            print('\nCongrats! The total subnets are ' + str(TotalSubnets2) + '\n')

    # Try this sliced numbers for the third octet
    try:
        if sub[8:11] == str(255):
            Uninteresting()
    
    # If it fails, finally try the remaining sliced numbers for the third octet
    finally:
        if sub[8:9] == str(0):
            Uninteresting()

        elif sub[4:5] == str(0):
            Uninteresting()

        elif sub[8:11] != str(255):
            magicNumber3 = 256 - int(sub[8:11])
            TotalSubnets3 = 256 / magicNumber3
        
            print('\nCongrats! The total subnets are ' + str(TotalSubnets3) + '\n')

   # Try this sliced numbers for the first octet
    try:
        if sub[12:15] == str(255):
            Uninteresting()
    
    # If it fails, finally try the remaining sliced numbers for the third octet
    finally:
        if sub[12:13] == str(0):
            Uninteresting()

        elif sub[6:7] == str(0):
            Uninteresting()

        elif sub[8:9] == str(0):
            Uninteresting()

        elif sub[10:] == str(0):
            Uninteresting()

        elif sub[12:15] != str(255):
            magicNumber4 = 256 - int(sub[12:15])
            TotalSubnets4 = 256 / magicNumber4
        
            print('\nCongrats! The total subnets are ' + str(TotalSubnets4) + '\n')

    
if __name__ == "__main__":
    subnets()