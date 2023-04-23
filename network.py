"this code snippet generates network usage by the machine"
import os
import psutil
from threading import Timer
from misce import*
import pandas as pd
import logging
#The function below converts bytes into KB, MB, GB etc respectively.
global df
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger() 
df = pd.DataFrame(columns= ['Id', 'Interface Name', 'IP Address', 'Broadcast IP', 'MAC Address', 'Netmask', 'Broadcast MAC', 'Total Bytes Sent', 'Total Bytes Received', 'timestamp'])
def net_info():
    net = []
    file_name = os.path.join(dirs[1], "network_insights.csv")
    def net_func():
        logger.info("Fetching network interface metrics")
        net_io = psutil.net_io_counters()
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for i, address in enumerate(interface_addresses):
                if str(address.family) == 'AddressFamily.AF_INET' or str(address.family) == 'AddressFamily.AF_PACKET':
                    network_info = {'Id':"Interface No."+str(i), "Interface Name": interface_name, "IP Address": address.address, "Broadcast IP": address.broadcast, "MAC Address": address.address, 
                    "Netmask": address.netmask, "Broadcast MAC": address.broadcast, "Total Bytes Sent": get_size(net_io.bytes_sent), "Total Bytes Received": get_size(net_io.bytes_recv), "timestamp" : str(get_timestamp())}
        net.append(network_info)
        df = pd.DataFrame(net)
        df.to_csv(file_name)
        compress_file(file_name)
        logger.info("cycle over fetched network interface metrics")
        Timer(5, net_func).start()
    net_func()
net_info()
