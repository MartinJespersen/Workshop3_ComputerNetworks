import socket
import sys
import datetime

address = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.sendto(''.encode(), (address, port))
msg, addressport = s.recvfrom(4)

print(msg)
msg_int = int.from_bytes(msg, 'big')
print(msg_int)
dt = datetime.datetime.fromtimestamp(msg_int)
print(dt)
