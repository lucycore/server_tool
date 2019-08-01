import socket
import os

#声明主机
host = ""
#声明端口号
port = 2323
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环

cli, addr = sock.accept()
print("连接完成")
path = r"C:\Users\lucycore\Desktop\server_tool\a.txt"

f = open(path,"wb")

while True:
	a = cli.recv(2048)
	
	
	f.write(a)

f.close()
print("完成")


#mod = cli.recv(2048).decode()

#cli.sendall("6.3".encode())

