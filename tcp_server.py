import socket	
import time	
import sys	
from datetime import datetime, timezone, timedelta


s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)		
print ("Socket successfully created")

port = int(sys.argv[1])			
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		

while True:
    c, addr = s.accept()	
    print ('Got connection from', addr)

    atmos_epoch = datetime(1900, 1, 1, 0, 0, tzinfo=timezone.utc)
    delta_time = datetime.now(timezone.utc) - atmos_epoch
    time_in_sec = int(delta_time.total_seconds())
    print('Datetime send: ', delta_time)
    print('Seconds send: ', time_in_sec)
    time_in_bytes = time_in_sec.to_bytes(4, byteorder='big')
    mes = c.send(time_in_bytes)
    
    c.close()
    break
