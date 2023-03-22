import socket
import sys
from datetime import datetime, timedelta, timezone

address = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.sendto(b'', (address, port))
msg, addressport = s.recvfrom(4)

print(msg)
msg_int = int.from_bytes(msg, 'big')
time_delta = timedelta(seconds=msg_int)
current_datetime = time_delta + datetime(1900, 1, 1, 0, 0, tzinfo=timezone.utc)
print(current_datetime)