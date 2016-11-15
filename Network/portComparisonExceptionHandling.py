import socket
connectionTimeout = int(input('What length of connection timeout would you like to use? (Enter # representing seconds)'))
socket.setdefaulttimeout(connectionTimeout)
port = int(input('What port number would you like to connect to? '))
ipAddress = input('What IP address would you like to connect to? ')
socketVar = socket.socket()
try:
	socketVar.connect((ipAddress,port))
except Exception, e:
	print "[-]: Error = "+str(e)
	quit()
readBanner = socketVar.recv(1024)
if ("FreeFloat Ftp Server (Version 1.00)" in readBanner):
	print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in readBanner):
	print "[+] 3Com 3CDaemon FTP Server is vulnerable."
elif ("Ability Server 2.34" in readBanner):
	print "[+] Ability FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in readBanner):
	print "[+] Sami FTP Server is vulnerable."
else:
	print "[-] FTP Server passes check."







