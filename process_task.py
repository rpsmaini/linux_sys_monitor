#!/usr/bin/python3
#Imports
from os import *
import psutil
from threading import Timer
from misce import get_timestamp
import pandas as pd
from datetime import date
from datetime import timedelta
import os
import shutil
from time import sleep
from misce import *

global df
global file_name
global d_str
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
#print((dirs[0]))
df = pd.DataFrame(columns=['pid', 'process_name', 'user', 'memory_used%', 'cpu_used%', 'timestamp'])
file_name = os.path.join(dirs[1], "process_log.csv")
#json_file = os.path.join(dirs[1], "process_log.json")
def proc():
    def tasks_running() :
        logger.info("fetching process metrics")
        proc_list = []
        def proc_func():
            for process in [psutil.Process(pid) for pid in psutil.pids()]:
                try :
                    procs = {"pid" : str(process.ppid()),"process_name" : str(process.name()),"user" : str(process.username()),
                        "memory_used%" : str(process.memory_percent())+"%","cpu_used%" : str(process.cpu_percent())+"%","timestamp" : str(get_timestamp())}
                except psutil.NoSuchProcess:
                    logger.warning("Process is killed : " + str(process.ppid()))
                    print("Some Process killed")
                    #log_func.logger.info("process got killed")
                proc_list.append(procs)
            df = pd.DataFrame(proc_list)
            df.to_csv(file_name)
            compress_file(file_name)
            logger.info("cycle over processes data updated")
            Timer(5, proc_func).start()
        proc_func()
        sleep(6)
    tasks_running()
    def checkdate():
        #this function will be called after every 24 hrs and file will be appended in date folder
        today = date.today()
        yesterday = str(today - timedelta(1))
        if today == yesterday:
            d_str = os.path.join(dirs[5], yesterday)
            os.makedirs(d_str, exist_ok=True)
            print(file_name ,d_str)
            shutil.move(file_name, d_str)
            shutil.move('log.txt', d_str)
            logger.info("data sent to date folder")
        else:
            logger.info("the day is still same")
        Timer(3600, checkdate).start()
    checkdate()
proc()
