import time

import socket



#声明主机
host = ""
#声明端口号
port = 2233
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环


while True:
	print("服务器控制程序启动！")
	cli, addr = sock.accept()
	print("客户端接入")

	print(cli.recv(1024).decode("utf-8"))

	cli.sendall("stop".encode("utf-8"))

	print(cli.recv(1024).decode("utf-8"))

	cli.sendall("stop".encode("utf-8"))





