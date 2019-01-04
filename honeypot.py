import socket
import time
import os
import sys

banner = r'''
Coded by sc1341
 /$$   /$$                                                        /$$                        
| $$  | $$                                                       | $$                        
| $$  | $$ /$$$$$$ /$$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$  /$$$$$$ /$$$$$$     /$$$$$$ /$$   /$$
| $$$$$$$$/$$__  $| $$__  $$/$$__  $| $$  | $$/$$__  $$/$$__  $|_  $$_/    /$$__  $| $$  | $$
| $$__  $| $$  \ $| $$  \ $| $$$$$$$| $$  | $| $$  \ $| $$  \ $$ | $$     | $$  \ $| $$  | $$
| $$  | $| $$  | $| $$  | $| $$_____| $$  | $| $$  | $| $$  | $$ | $$ /$$ | $$  | $| $$  | $$
| $$  | $|  $$$$$$| $$  | $|  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$/ |  $$$$/$| $$$$$$$|  $$$$$$$
|__/  |__/\______/|__/  |__/\_______/\____  $| $$____/ \______/   \___/|__| $$____/ \____  $$
                                     /$$  | $| $$                         | $$      /$$  | $$
                                    |  $$$$$$| $$                         | $$     |  $$$$$$/
                                     \______/|__/                         |__/      \______/ 
'''

class Honeypot:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def __init__(self,HOST,PORT):
		self.s.bind((HOST,PORT))
		self.s.listen(100)

	def listen(self):
		'''Recieves the connection and logs the time, it then takes the data that is sent by the client, 
		and logs it in the "honeypotlog.txt file'''
		while True:
			conn, addr = self.s.accept()
			print("Connection from {}".format(addr))
			localtime = time.asctime(time.localtime(time.time()))
			data = conn.recv(1024)
			if not data:
				break
			else:
				data = data.decode()
			conn.sendall(b'Hello there')
			self.log(data,addr,localtime)


	def log(self,data,addr,time):
		line = "="
		try: 
			f = open('honeypotlog.txt','w')
			f.close()
		except:
			pass
		with open('honeypotlog.txt','a') as f:
			f.write(line * 25)
			f.write("\n")
			f.write("Time: "+time+"\n")
			f.write("Data: "+ data+"\n")
			f.write("Address: "+str(addr)+"\n")
		f.close()

	def run(self):
		'''Runs the program by calling the listen function'''
		while True:
			self.listen()

if len(sys.argv) == 1:
	print(banner)
	print("Need 2 arguments, the address and port of the honeypot")
	sys.exit()
else:
	pass

print(banner)
try:
	honeypot = Honeypot(sys.argv[1],int(sys.argv[2]))
except OSError:
	print("ERROR: That address is already in use, please use a different one")




