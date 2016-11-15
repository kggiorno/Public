import socket

# initialize host and socket via user input

target_host = input("What is the exact target host IP address?")
target_socket = input("What is the exact target port?")

# create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data

client.sendto("AAABBBCCC",(target_host,target_port))

# receive some data

data, addr = client.recvfrom(4096)

print data