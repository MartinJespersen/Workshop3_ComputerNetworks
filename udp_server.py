import socket
import sys
import time
from datetime import datetime, timedelta, timezone

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

port = int(sys.argv[1])

s.bind(('', port))
print("UDP server up and listening")

while(True):
    msg, address = s.recvfrom(1)

    atmos_epoch = datetime(1900, 1, 1, 0, 0, tzinfo=timezone.utc)
    d = datetime.now(timezone.utc) - atmos_epoch
    time_in_sec = int(d.total_seconds())
    print('Datetime send: ', d)
    print('Seconds send: ', time_in_sec)
    time_in_bytes = time_in_sec.to_bytes(4, byteorder='big')
    s.sendto(time_in_bytes, address)