import socket	
import time	
import sys	

s = socket.socket()		
print ("Socket successfully created")

port = int(sys.argv[1])			
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		

while True:
    c, addr = s.accept()	
    print ('Got connection from', addr)

    time_in_sec = int(time.time())
    time_in_bytes = time_in_sec.to_bytes(4, byteorder='big')
    mes = c.send(time_in_bytes)
    
    c.close()
    break
