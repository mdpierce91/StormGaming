import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

x=0
message = []

while True:
	data, addr = sock.recvfrom(4096)
	print "received message:\n", x
	message.append(data)
	x=x+1
#take the last message and read the time out of it and compare it to now to get the sending time**CURRENTLY DISABLED**
#start_str = message[-1]
#start = float(start_str)
#end = (time.time())*1000
#print "."+message[-1]
#print end, "\n", end-start
exit(1)
