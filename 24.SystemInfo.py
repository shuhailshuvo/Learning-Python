import os
import math
from psutil import virtual_memory, disk_partitions, disk_usage, net_if_addrs
import time
import ctypes

print("Operating System: ", os.sys.platform)
print("Number of CPU: ", os.cpu_count())
mem = virtual_memory()
print("Physical Memory:", math.ceil(mem.total/1024/1024/1024), "GB")
drives = disk_partitions()
print("Number of Drive Partition:", len(drives))
for drive in drives:
    disk = disk_usage(drive.device)
    print("Total Space in ", drive.device,
          math.ceil(disk.total/1024/1024/1024), "GB")

print("File system encoding: ", os.sys.getfilesystemencoding())
print("System Path: ", os.path)
print("Current Directory: ", os.getcwd())
print("User name: ", os.getlogin())

print("Environmental Variables: \n", os.environ)

net = net_if_addrs()


print(net['Ethernet 2'])


choice = ctypes.windll.user32.MessageBoxW(
    0, "Do you want to lock your screen?", "With your Permission", 0x40 | 0x1)

if choice == 1:
    ctypes.windll.user32.LockWorkStation()
else:
    print("Ok! Then shutting it Down")
    time.sleep(2)
    os.system("shutdown /s /t 1")
