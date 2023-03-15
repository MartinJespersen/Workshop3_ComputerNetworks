import socket 
import sys
import datetime

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

port = int(sys.argv[2])
host_ip = sys.argv[1]

s.connect((host_ip, port))

msg = s.recv(4)
print(msg)
msg_int = int.from_bytes(msg, 'big')
print(msg_int)
dt = datetime.datetime.fromtimestamp(msg_int)
print(dt)

