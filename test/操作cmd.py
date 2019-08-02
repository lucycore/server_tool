import os

p = os.popen("dir")
a = str(p.read())
#print(a)

p = os.popen("cd ./Desktop")
a = str(p.read())
print(a)

p = os.popen("dir")
a = str(p.read())
print(a)

