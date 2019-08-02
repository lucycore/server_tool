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

while True:

	cli, addr = sock.accept()
	print("连接完成")

	cmd = cli.recv(1024).decode("utf-8")

	if cmd == "up":

		cli.sendall("服务器反馈：已接入上传模块".encode("utf-8"))

		filename = cli.recv(1024).decode("utf-8")
		cli.sendall("服务器反馈：已接收文件路径".encode("utf-8"))

		filesize = int(cli.recv(1024).decode("utf-8"))
		cli.sendall("服务器反馈：已接收文件大小".encode("utf-8"))

		f = open(filename,"wb")

		size_s = 0
		while filesize != 0:

			if size_s < filesize:
				size_s = 1024
			else:
				size_s = filesize

			a = cli.recv(filesize)
			f.write(a)
			filesize = filesize - size_s

		f.close()

		print("完成")


	if cmd == "get":

		cli.sendall("服务器反馈：已接入下载模块".encode("utf-8"))

		filepath = cli.recv(1024).decode("utf-8")
		
		#获取文件大小
		size = os.stat(filepath).st_size
		#并发送
		cli.sendall(str(size).encode("utf-8"))

		f = open(filepath,"rb")

		for x in f:

			cli.sendall(x)

		print("发送完成")

		f.close()

		

