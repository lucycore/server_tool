import os

all_list = []
for root , dirs, files in os.walk(r"C:\Users\lucycore\Desktop\server_tool"):
	for x in files:
		z = root + "\\" + x
		all_list.append(z)

for x in all_list:
	print(x)


dirs = os.listdir(r"C:\Users\lucycore\Desktop\server_tool")


print(dirs)

input()