import socket
import sys
import time

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

port = int(sys.argv[1])

s.bind(('', port))
print("UDP server up and listening")

while(True):
    msg, address = s.recvfrom(1)

    time_in_sec = int(time.time())
    time_in_bytes = time_in_sec.to_bytes(4, byteorder='big')
    s.sendto(time_in_bytes, address)