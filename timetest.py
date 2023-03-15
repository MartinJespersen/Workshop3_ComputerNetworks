import time
import sys
time_in_sec = int(time.time())
time_in_bytes = time_in_sec.to_bytes(4, byteorder='big')
print(time_in_bytes)

print(time_in_sec)
print('Number of bytes:', len(time_in_bytes))
