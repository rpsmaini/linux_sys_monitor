#!/usr/bin/python3
"""This is main.py used for calling other python Files containing different 
Components/Functions"""
import os

#from gpu_usage import gpu_insights
os.system('pip3 install -r requirements.txt')
# Importing Modules
from threading import Thread
from time import sleep
from process_task import proc
from onetime_info import sys
from overall import get_load
#from ram_usage import fetch_mu
#from network import net_info
#from cpu_usage import cpu_util
from misce import *

#calling subfuntions to generate reports
def menu():
    dirs = initializer()# function for createing directory
    logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
    logger = logging.getLogger()
    sleep(1)
    try :
        logger.info("Initializing system metrics")
        print("starting to monitor process")
        thread_1 = Thread(target=proc)
        thread_2 = Thread(target=sys)
        thread_3 = Thread(target=get_load)
        #thread_4 = Thread(target=fetch_du)
        #thread_5 = Thread(target=net_info)
        #thread_6 = Thread(target=cpu_util)
        #thread_7 = Thread(target=gpu_insights)
        thread_1.start()
        thread_2.start()
        thread_3.start()
        #thread_4.start()
        #thread_5.start()
        #thread_6.start()
        #thread_7.start()
    except:
        print(KeyboardInterrupt("Exiting program explicitly"))
        print("system encountered some error")
        thread_1.kill()
        thread_2.kill()
        thread_3.kill()
        #thread_4.kill()
        #thread_5.kill()
        #thread_6.kill()
        #thread_7.kill( )
        exit()
menu()
