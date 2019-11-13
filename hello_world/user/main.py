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


	def cdi(self):
		#用来进入新的位置的函数
		print(self.path)
		self.path.append(self.patha)
		print(self.path)
		path = "\\".join(self.path)
		return path


	def cdq(self):
		#用来退出文件位置的函数
		del self.path[-1]
		path = "\\".join(self.path)
		return path


	def cd(self):
		#用来跳跃文件的位置
		return None


	def rmr(self):
		#用于递归删除路径的函数
		path = "\\".join(self.path)
		path = path + "\\" + self.patha
		dir = path.replace('\\', '/')
		if(os.path.isdir(dir)):
			for p in os.listdir(dir):
				remove_dir(os.path.join(dir,p))
			if(os.path.exists(dir)):
				os.rmdir(dir)
		else:
			if(os.path.exists(dir)):
				os.remove(dir)
		return None


	def rm(self):
		#用于单个删除文件的函数
		path = "\\".join(self.path)
		path = path + "\\" + self.patha
		os.remove(dir)
		return None


	def mv(self):
		#用于移动文件的函数
		path = self.path
		new_path = "\\".join(self.path)
		new_path = new_path + "\\" + self.patha
		shutil.move(path,new_path)


	def ls(self):
		#用于列出此目录下文件的函数
		path = "\\".join(self.path)
		all_list = []
		for root , dirs, files in os.walk(path):
			for x in files:
				z = root + "\\" + x
				all_list.append(z)

		all_list = str(all_list)
		return all_list




def cmdx(cmd):

	if cmd[0] == "ls":
		p = core.ls()
		print(p)

	if cmd[0] == "we":
		p = core.where_i_am()
		print(p)

	if cmd[0] == "cdi":
		core.patha = cmd[1]
		p = core.cdi()


	if cmd[0] == "cdq":
		p = core.cdq()


	if cmd[0] == "rm":
		core.patha = cmd[1]
		p = core.rm()


	if cmd[0] == "rmr":
		core.patha = cmd[1]
		p = core.rmr()

'''
	if cmd[0] == "":
	if cmd[0] == "":

'''
core = WinControl()
while True:

	cmd = input(">>")
	cmd = cmd.split(' ')
	cmdx(cmd)



























