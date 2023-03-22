import socket 
import sys
from datetime import datetime, timezone, timedelta

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
time_delta = timedelta(seconds=msg_int)
current_datetime = time_delta + datetime(1900, 1, 1, 0, 0, tzinfo=timezone.utc)
print(current_datetime)


