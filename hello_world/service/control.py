
import psutil
 
def find(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print(pid)
            break
    else:
        print("not found")
        
find("shabi")
