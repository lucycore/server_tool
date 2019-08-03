import socket
import time

while True:
	sock = socket.socket()
	HOST = "104.155.212.130"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("hi".encode())
	server = sock.recv(1024).decode()

	print(server)

	sock.sendall("hi".encode())

	print(sock.recv(1024).decode())

	while True:

		cmd = input(">>")

		sock.sendall(cmd.encode())
		print(sock.recv(1024).decode())


	time.sleep(5)