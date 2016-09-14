import socket

target_host = input("What is the exact target URL?")
target_port = input('What is the exact target port?')

# create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client

client.connect((target_host,target_port))

# send some data

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data

response = client.recv(4096)

print response