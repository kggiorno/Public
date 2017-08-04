import socket
import sys

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

# Datagram (udp) socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print('Socket created')
except socket.error, msg:
	print('Failed to create socket. Error code: {} Message {}'.format(str(msg[0]),msg[1]))
	sys.exit()
	
# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print('Bind failed. Error code: {} Message {}'.format(str(msg[0]), msg[1]))
	sys.exit()

print('Socket bind complete')

# Now keep talking with client
while True:
	# Receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]

	if not data:
		break

	reply = 'OK... {}'.format(data)

	s.sendto(reply, addr)
	print('Message[{}:{}] - {}'.format(addr[0],str(addr[1]),data.strip()))

	s.close()	