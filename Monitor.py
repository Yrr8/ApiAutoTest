"""
监控代码;监控服务器的内存、cpu、网络、磁盘等，与租车系统部署在一起
"""
import time
from datetime import datetime

import psutil

print(psutil.cpu_percent())  # 获取cpu信息
print(psutil.virtual_memory())  # 虚拟内存
print(psutil.virtual_memory().percent)  # 虚拟内存百分比
print(psutil.disk_usage("d:/"))  # 租车系统所在的磁盘的百分比
print(psutil.disk_usage("d:/").percent)  # 租车系统所在的磁盘的百分比
print(psutil.net_io_counters())  # 网络
print(psutil.net_io_counters().bytes_sent)
print(psutil.net_io_counters().bytes_recv)

with open("d:/资源占用情况.txt", encoding='utf-8', mode='w') as file:
    file.write("时间戳\t\t\t\tCPU%\t内存%\t磁盘%\t发送字节数\t接收字节数\n")
    while True:
        print("监控中............")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\t")
        file.write(str(psutil.cpu_percent()) + "%\t")
        file.write(str(psutil.virtual_memory().percent) + "%\t")
        file.write(str(psutil.disk_usage("d:/").percent) + "\t")
        file.write(str(psutil.net_io_counters().bytes_sent) + "\t")
        file.write(str(psutil.net_io_counters().bytes_recv) + "\n")
        file.flush()
        time.sleep(3)
