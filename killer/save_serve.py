import socket
import os

#声明主机
host = ""
#声明端口号
port = 5000
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环

print("服务器控制程序启动！")

while True:
	try:
		cli, addr = sock.accept()
		print("客户端接入")

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
			
	except:
		print("e")

	