import socket
import os


def help():

	print("-con [ip] 连接服务器")
	print("-get [server_path] [path] 从服务器下载单个文件")
	print("-up [path] [server_path] 从服务器上传单个文件")
	print("")
	print("")
	print("")



def main():

	print("服务器socket传输程序")

	while True:

		cmda = input(">>")

		if len(cmda)==0: continue  # 如果传入空字符会阻塞

		try:
			cmdlist = cmda.split(' ')
		except:
			print("e")


		if cmdlist[0] == "help":
			help()

		elif cmdlist[0] == "con":

			sock = socket.socket()
			HOST = cmdlist[1]
			PORT = 2233
			sock.connect((HOST, PORT))

			print("已连接服务器")

		elif cmdlist[0] == "up":

			#=======================================
			sock.send(cmdlist[0].encode("utf-8"))
			#打印服务器反馈
			server_reply = sock.recv(1024).decode("utf-8")
			print(str(server_reply))
			#=======================================

			f = open(cmdlist[1],"rb")

			sock.send(cmdlist[2].encode("utf-8"))

			#打印服务器反馈
			server_reply = sock.recv(1024).decode("utf-8")
			print(str(server_reply))


			size = os.stat(cmdlist[1]).st_size #获取文件大小
			#发送文件大小 

			sock.send(str(size).encode("utf-8"))

			#打印服务器反馈
			server_reply = sock.recv(1024).decode("utf-8")
			print(str(server_reply))

			for x in f:
				sock.send(x)


			print("发送完成")

			#打印服务器反馈
			server_reply = sock.recv(1024).decode("utf-8")
			print(str(server_reply))


		elif cmdlist[0] == "get":

			#=======================================
			sock.send(cmdlist[0].encode("utf-8"))
			#打印服务器反馈
			server_reply = sock.recv(1024).decode("utf-8")
			print(str(server_reply))
			#=======================================

			#发送服务器文件路径
			sock.send(cmdlist[1].encode("utf-8"))

			filesize = int(sock.recv(1024).decode("utf-8"))
			size = 1024

			f = open(cmdlist[2],"wb")

			while filesize != 0:
				if filesize > size:
					size = 1024
				else:
					size = filesize

				f_line = sock.recv(size)
				f.write(f_line)

				filesize = filesize - size
				print(filesize)

			f.close()
			print("接收完成")



main()

