import socket
import os

path = r"C:\Users\lucycore\Desktop\hello.txt"


sock = socket.socket()
HOST = "192.168.0.11"
PORT = 2323
sock.connect((HOST, PORT))
#发送模式
print("连接完成")
f = open(path,"rb")

for x in f:
	sock.sendall(x)

sock.sendall("over".encode())
print("完成")


'''
sock.sendall("update".encode())
server_myd = sock.recv(1024).decode()
#发送id
sock.sendall(user_id.encode())
#接受服务器的状态码
server_s = sock.recv(1024).decode()
sock.close()


'''
