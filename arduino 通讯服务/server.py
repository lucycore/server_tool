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
	try:
		#堵塞连接
		cli, addr = sock.accept()
		print("\n\n客户端接入！")
		print(addr)

		#接收模式识别
		mod = cli.recv(2048).decode()

		#模式为验证更新
		if mod == "SXY":
			cli.sendall("3".encode())
			js = 0
			for x in range(3):
				js += 1
				a = cli.recv(2048).decode()
				cli.sendall(str(js).encode())

			
