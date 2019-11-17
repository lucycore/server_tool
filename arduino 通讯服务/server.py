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
