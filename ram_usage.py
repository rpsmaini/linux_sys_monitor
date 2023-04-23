"""This code generates and shows the ram consumption by the machine"""
import psutil
import os
from threading import Timer
from misce import*
import pandas as pd
import logging
global df
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
df = pd.DataFrame(columns= ['Total RAM', 'Available RAM', 'Used RAM', 'Used Precentage', 'Swap Memory Total', 'Swap Memory Used', 'Swap Memory Free', 'Swap Used Precntage', 'timestamp'])
file_name = os.path.join(dirs[1], "ram_insights.csv")
def fetch_mu():
    logger.info("fetching memory metrics")
    ram_usage = []
    ## Memory Information
    def ram_entity():
        logging.info("fetching ram metrics")
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        ram_info = {"Total RAM" : get_size(svmem.total),"Available RAM" : get_size(svmem.available),"Used RAM" : get_size(svmem.used),"Used Precentage" : str(svmem.percent)+ "%","Swap Memory Total" : get_size(swap.total),
            "Swap Memory Used" : get_size(swap.used),"Swap Memory Free" : get_size(swap.free),"Swap Used Precntage" : str(swap.percent) +"%","timestamp" : str(get_timestamp())}
        ram_usage.append(ram_info)
        df = pd.DataFrame(ram_usage)
        df.to_csv(file_name)
        compress_file(file_name)
        logger.info("cycle over fetched memory metrics!!")
        Timer(5, ram_entity).start()
    ram_entity()
fetch_mu()