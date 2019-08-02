import socket
import time

while True:
	sock = socket.socket()
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("i'm your father".encode())
	server = sock.recv(1024).decode()

	print(server)

	sock.sendall("i'm your father".encode())

	print(sock.recv(1024).decode())

	while True:

		cmd = input(">>")

		sock.sendall(cmd.encode())
		print(sock.recv(1024).decode())





	time.sleep(5)