import os
import psutil
import time
from datetime import datetime


os.system("cls")



def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
date = datetime.now().strftime("%Y-%m-%d")
new_date = date
while True:
    date_log = new_date + ".txt"
    with open(date_log, "a") as logfile:
        while True:
            new_date = datetime.now().strftime("%Y-%m-%d")
            if new_date != date:
                date = new_date
                break
            log_data = []
            log_data.append("="*20 + " Date" + "="*20)
            log_data.append(new_date)
            log_data.append("="*20 + " Time" + "="*20)
            log_data.append(datetime.now().strftime("%H:%M:%S"))
            log_data.append("="*20 + " CPU Info " + "="*20)
            log_data.append(f"Total CPU Usage: {psutil.cpu_percent()}%") 
            log_data.append("="*20 + " Memory Info " + "="*20)
            svmem = psutil.virtual_memory()
            log_data.append(f"Total: {get_size(svmem.total)}")
            log_data.append(f"Available: {get_size(svmem.available)}")
            log_data.append(f"Used: {get_size(svmem.used)}")
            log_data.append(f"Percentage: {svmem.percent}%")
            log_data.append("="*20 + " Disk Info " + "="*20)
            partitions = psutil.disk_partitions()
            for partition in partitions:
                log_data.append(f"=== Device: {partition.device} ===")
                log_data.append(f"  Mountpoint: {partition.mountpoint}")
                log_data.append(f"  File system type: {partition.fstype}")
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                log_data.append(f"  Total Size: {get_size(partition_usage.total)}")
                log_data.append(f"  Used: {get_size(partition_usage.used)}")
                log_data.append(f"  Free: {get_size(partition_usage.free)}")
                log_data.append(f"  Percentage: {partition_usage.percent}%")
            
            log_data.append("="*20 + " Network Info " + "="*20)
            net_io = psutil.net_io_counters()
            log_data.append(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
            log_data.append(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
            log_data.append("\n\n")
            for data in log_data:
                print(data)
            logfile.write("\n".join(log_data) + "\n\n")
            
            logfile.flush()
            time.sleep(30)
