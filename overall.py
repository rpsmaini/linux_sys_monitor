from genericpath import getsize
import os
import psutil
from threading import Timer
from misce import *
import pandas as pd
import logging
import GPUtil as GPU
import shutil
from datetime import*
global df
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"),level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode='a')
logger = logging.getLogger()
df = pd.DataFrame(columns=['CpuLoad', 'DiskLoad', 'MemoryLoad', 'BytesSend','BytesRecived', 'GpuLoad','timestamp'])
dirs = initializer()
def get_load():
    load = []
    file_name = os.path.join(dirs[1], "SystemLoad.csv")
    root_vol = psutil.disk_partitions()[0][1]
    svmem = psutil.virtual_memory()
    GPUs = GPU.getGPUs()
    #gpu=GPUs[0]
    net_io = psutil.net_io_counters()
    BytesRecived=net_io.bytes_recv
    BytesSend=net_io.bytes_sent
    avg=(BytesRecived+BytesSend)/2
    navg = get_size(avg)
    def load_func():
        load_dict = {
            "Current_Time":str(get_timestamp()),
            #"'[GPU Load(in %),GPU Free Memory,GPU Used Memory,GPU Temperature(in C)]'":[("{2:3.0f}%, {0:.0f}MB, {1:.0f}MB, {3:.0f}°C".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil * 100,gpu.temperature))],
            "Network_Load(MB)":str(navg),
            "Cpu Load(in %)":str(psutil.cpu_percent()) + "%",
            "Memory Load(in %)":str(svmem.percent) + "%",
            "CPU Temprature":str(psutil.sensors_temperatures()),
            "Disk Load(in %)":str(psutil.disk_usage(root_vol)[-1]) + "%",
        }
        load.append(load_dict)
        df = pd.DataFrame(load)
        df.to_csv(file_name)
        compress_file(file_name)
        logger.info("cycle over fetched interface metrics")
        Timer(5, load_func).start()
    load_func()

    def sysfunc():
        today = date.today()
        yesterday = str(today - timedelta(hours=24))
        if today == yesterday:
            d_str = os.path.join(dirs[5], yesterday)
            os.makedirs(d_str, exist_ok=True)
            print(file_name, d_str)
            shutil.move(file_name, d_str)
            shutil.move('log.txt', d_str)
            logger.info("file sent to date folder")
        Timer(3600, sysfunc).start()

    sysfunc()
get_load()
