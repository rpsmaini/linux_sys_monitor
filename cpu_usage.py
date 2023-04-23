"""This code snippet shows realtime cpu usage and its related information"""
import cpuinfo
import psutil
from threading import Timer
import pandas as pd
from misce import *
global df
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
df = pd.DataFrame(columns=['Processor Name', 'Processor type', 'Physical cores', 'Total cores', 'Max Frequency', 'Min Frequency', 'Current Frequency', 'Total_cpu_usage', 'Per_core_use', 'timestamp'])
#main code
def cpu_util():
    logger.info("fetching cpu metrics")
    cpu_lst=[]
    cpufreq = psutil.cpu_freq()
    single_core_use ={}
    file_name = os.path.join(dirs[1], "cpu_insights.csv")
    def cpu_func():
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            single_core_use["Core "+str(i+1)] = str(percentage)+"%"
        cpu_info = {"Processor Name" : str(cpuinfo.get_cpu_info()['brand_raw']),"Processor type" : str(cpuinfo.get_cpu_info()['arch']),"Physical cores" : str(psutil.cpu_count(logical=True)),"Total cores" : str(psutil.cpu_count(logical=True)),"Max Frequency" : str(cpufreq.max)+"Mhz",
            "Min Frequency": str(cpufreq.min)+"Mhz","Current Frequency" : str(cpufreq.current)+"Mhz","Total_cpu_usage" :str(psutil.cpu_percent())+"%","Per_core_use" : single_core_use,"timestamp" : get_timestamp()}
        cpu_lst.append(cpu_info)
        #print(cpu_info.keys())
        df = pd.DataFrame(cpu_lst)
        df.to_csv(file_name)
        compress_file(file_name)
        logger.info("cycle over fetched all cpu metrics!!")
        Timer(5, cpu_func).start()
    cpu_func()
cpu_util()    