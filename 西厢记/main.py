import socket

zt = input("请输入‘start’or‘stop’:")

sock = socket.socket()
HOST = "167.179.65.135"
PORT = 2233
sock.connect((HOST, PORT))
print("服务器连接完成")


#发送模式
sock.sendall("core".encode())
my = sock.recv(1024).decode()


sock.sendall(zt.encode())

print(sock.recv(1024).decode())
sock.close()