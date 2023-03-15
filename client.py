# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 12345
host_ip = "10.192.75.10"

# connecting to the server
s.connect((host_ip, port))
mes = s.recv(1000)
print(mes)
print ("client stops")
