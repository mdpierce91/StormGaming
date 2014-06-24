import socket
import sys
import time

#get the number of frames specified in the arguements of the call, use 1 as a default if one isn't given
if len(sys.argv) == 1:
	print 'please enter the number of frames you wish to send, for example \"python udpbmpsend.py 60\" the default of 1 will be used if no number is given'
	FPS = 1
else:
	FPS = int(sys.argv[1])
	print FPS

UDP_IP = "127.0.0.1"
UDP_PORT = 8000

#Get the current time, save it into start
start = time.time()
start = start*1000
print start
str_start = repr(start)
print str_start

#loop the number of frames you want to send
loop = 0
while loop < FPS:
	#open the constructed file
	message_location = open("binarynumber.txt")
	message= ""
	#read in and send each line from the constructed file
	for line in message_location:
		message = line.replace("\n","")

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(message, (UDP_IP, UDP_PORT))
	y=y+1
		
#send a last packet containing the start time of the program **CURRENTLY DISABLED**
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(str_start, (UDP_IP, UDP_PORT))

#get the time after sending all the files, output the difference
end = time.time()
end = end*1000
print end
print end-start, 'ms'
print "finished"