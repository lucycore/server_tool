import socket
import time


sock = socket.socket()
HOST = "127.0.0.1"
PORT = 2233
sock.connect((HOST, PORT))
js = 0
while True:
	input("sent")
	js += 1
	a = "heart" + str(js)
	sock.send(a.encode("utf-8"))
	#print(sock.recv(1024).decode("utf-8"))
	


