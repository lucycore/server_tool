import socket
import os

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

print("服务器控制程序启动！")
cli, addr = sock.accept()
print("客户端接入")
while True:

	input("a")
	print(cli.recv(1024).decode("utf-8"))

	#cli.sendall("服务器反馈：已接入上传模块".encode("utf-8"))


