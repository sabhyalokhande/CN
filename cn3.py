def convert_to_binary(num):
    answer = ""
    while num != 0:
        answer = str(num % 2) + answer
        num = num // 2
    while len(answer) != 8:
        answer = "0" + answer
    return answer

print("This assignment decodes a class C IP address")
print("Enter the initial IP (192.B.C.D format):", end="")
input_ip_1 = input()
sections = input_ip_1.split('.')

print("The IP address in bits format is: ")
prelim_string = ""
prelim_bitwise = ""
for i in range(0, 4):
    if i != 3:
        print(convert_to_binary(int(sections[i])) + ".", end="")
        prelim_bitwise = prelim_bitwise + convert_to_binary(int(sections[i])) + "."
        prelim_string = prelim_string + sections[i] + "."
    else:
        print(convert_to_binary(int(sections[i])), end="\n")
        prelim_bitwise = prelim_bitwise + convert_to_binary(int(sections[i]))
        prelim_string = prelim_string + sections[i]

cidr = -1
while cidr > 32 or cidr < 24:
    cidr = int(input("Enter the CIDR bits (a number between 24 to 31): "))

last_bits = cidr - 24
temp = 0
for i in range(last_bits):
    temp = temp + 2**(7 - i)

print("Subnet mask in numeric format: 255.255.255." + str(temp))
print("Subnet mask in bitwise format: ", end="")
print(convert_to_binary(255) + "." + convert_to_binary(255) + "." + convert_to_binary(255) + "." + convert_to_binary(temp) + "\n")

network_num = int(sections[3]) & temp
broadcast_num = (255 - temp) | int(sections[3])

print("Network address in numeric format: " + prelim_string + str(network_num))
print("Network address in bitwise format: " + prelim_bitwise[:-8] + convert_to_binary(network_num) + "\n")

print("Broadcast address in numeric format: " + prelim_string + str(broadcast_num))
print("Broadcast address in bitwise format: " + prelim_bitwise[:-8] + convert_to_binary(broadcast_num) + "\n")

if broadcast_num - network_num > 1:
    print("First address in numeric format: " + prelim_string + str(network_num + 1))
    print("First address in bitwise format: " + prelim_bitwise[:-8] + convert_to_binary(network_num + 1) + "\n")
    
    print("Last address in numeric format: " + prelim_string + str(broadcast_num - 1))
    print("Last address in bitwise format: " + prelim_bitwise[:-8] + convert_to_binary(broadcast_num - 1) + "\n")
else:
    print("No usable address in this subnet")

while True:
    print("Enter the IP (192.B.C.D format) or exit (1):", end="")
    input_ip_2 = input()
    if input_ip_2 == '1':
        break
    sections2 = input_ip_2.split('.')
    
    print("IP-2 address in bits format is: ")
    prelim_string1 = ""
    for i in range(0, 4):
        if i != 3:
            print(convert_to_binary(int(sections2[i])) + ".", end="")
            prelim_string1 = prelim_string1 + sections2[i] + "."
        else:
            print(convert_to_binary(int(sections2[i])), end="\n")
            prelim_string1 = prelim_string1 + sections2[i]

    if sections[0:3] != sections2[0:3]:
        print("Clients are not in the same network")
    else:
        if int(sections2[3]) >= network_num and int(sections2[3]) <= broadcast_num:
            if int(sections2[3]) == int(sections[3]):
                print("Same IP address entered twice")
            else:
                print("Clients are in the same subnet! Connectivity can be established!")
        else:
            print("Clients are in the same network but different subnets, connectivity cannot be established.")
