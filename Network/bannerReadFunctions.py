import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(10)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):
	if 'FreeFloat Ftp Server (Version 1.00)' in banner:
		print '[+] FreeFloat FTP Server is vulnerable.'
	elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
		print '[+] 3CDaemon'