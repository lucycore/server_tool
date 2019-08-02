from urllib import request
import os
import zipfile

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

try:
	remove_dir(r"C:\sun32")
except:
	print("")

os.makedirs(r"C:\sun32\center\windows")

request.urlretrieve("http://www.lucycore.top/v2ray/lcv2Win.zip",r"C:\sun32\center\windows\c.zip")
azip = zipfile.ZipFile(r"C:\sun32\center\windows\c.zip")
#解压到原始目录
azip.extractall(r"C:\sun32\center\windows")

os.system(r"C:\sun32\center\windows\lcv2_V6.3.exe")