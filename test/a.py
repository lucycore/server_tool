import socket
import time

while True:
	sock = socket.socket()
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("i will go to die".encode())
	server = sock.recv(1024).decode()

	if server == "stop":
		sock.close()
	else:
		print("控制主机已接入！")
		while True:
			server = sock.recv(1024).decode()
			print(server)
			sock.sendall("i will go to die".encode())

	time.sleep(5)