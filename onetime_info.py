"""This Code Snippet Contains information related to system details"""
# Import modules
import os
from time import strftime
import cpuinfo
import psutil
import platform
import shutil
import pandas as pd
from threading import Timer
from datetime import *
from ssd_checker import is_ssd
from misce import *
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
global df
global d_str
df = pd.DataFrame(columns=['serial_no','user Name','system name','node name','system release',
 'system version','system machine','system processor','system total cores','system physical cores',
 'ssd availabe','Disk Size','ram size','boot time','fan Speed (rpm)','machine Temprature',
 'timestamp'])
#Main code
sys_lst = []
uname = platform.uname()
battery = psutil.sensors_battery()
boot_time_timestamp = psutil.boot_time()
booTime = datetime.fromtimestamp(boot_time_timestamp)
root_vol = psutil.disk_partitions()[0][0]
ssd = is_ssd(root_vol)
last_reboot = psutil.boot_time()
uptime = datetime.fromtimestamp(last_reboot)
mac = str(gma())
serial = mac.replace(":","")
root_vol = psutil.disk_partitions()[0][1]
svmem = psutil.virtual_memory()
file_name = os.path.join(dirs[1], "system.json")
def sys():
    def overview():
        logger.info("fetching overall system metrics")
        overall_sys_info = {
            "serial_no.": serial,
            "user name": str(os.getlogin()),
            "system_name": str(uname.system),
            "node Name": str(uname.node),
            "system release": str(platform.release()),
            "system version": str(uname.version),
            "system machine": str(uname.machine),
            "system processor": str(cpuinfo.get_cpu_info()['brand_raw']),
            "system total cores": str(psutil.cpu_count(logical=True)),
            "system physical cores": str(psutil.cpu_count(logical=False)),
            "ssd_availabe": str(ssd),
            'disk size': str(get_size(psutil.disk_usage(root_vol)[0])),
            'ram size': str(get_size(svmem.total)),
            "boot Time": str(uptime.strftime("%d-%m-%y %H:%M:%S")),
            "boot Date": str(uptime.strftime("%d-%m-%y")),
            "fan Speed (rpm)": str(psutil.sensors_fans()),
            "machine Temprature": str(psutil.sensors_temperatures()),
            "timestamp": str(get_timestamp())
        }
        sys_lst.append(overall_sys_info)
        df = pd.DataFrame(sys_lst)
        df.to_json(file_name,orient='records')# ,index=None)
        compress_file(file_name)
        logger.info("cycle over system data updated")
        Timer(7200, overview).start()
    overview()
    def sysfunc():
        today = date.today()
        yesterday = str(today - timedelta(hours= 24))
        if today == yesterday:
            d_str = os.path.join(dirs[5], yesterday)
            os.makedirs(d_str, exist_ok=True)
            print(file_name ,d_str)
            shutil.move(file_name, d_str)
            shutil.move('log.txt', d_str)
            logger.info("file sent to date folder")
        Timer(3600, sysfunc).start()
    sysfunc()
sys()
