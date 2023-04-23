import psutil
from threading import Timer
from misce import*
import pandas as pd

global df
df = pd.DataFrame(columns= ['Id', 'Device', 'Mountpoint', 'Filesystem', 'Total read', 'Total write', 'Total Size', 'Used', 'Free', 'Percentage', 'timestamp'])
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
def fetch_du():
    partitions = psutil.disk_partitions()
    disk_io = psutil.disk_io_counters()
    partition_usage_list = []
    file_name = os.path.join(dirs[1], "disk_insights.csv")
    def disk_entity():
        logger.info("fetching disk metrics")
        for i, partition in enumerate (partitions):
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
            #    # this can be catched due to the disk that
            #    # isn't ready
                pass
            disk_info = {
            "Id":"Disk "+str(i+1), "Device" : partition.device, "Mountpoint" : partition.mountpoint, "Filesystem" : partition.fstype, "Total read" : get_size(disk_io.read_bytes), "Total write" : get_size(disk_io.write_bytes),
                "Total Size" : get_size(partition_usage.total), "Used": get_size(partition_usage.used), "Free": get_size(partition_usage.free), "Percentage": str(partition_usage.percent)+"%", "timestamp" : str(get_timestamp())}
            partition_usage_list.append(disk_info)
        df = pd.DataFrame(partition_usage_list)
        df.to_csv(file_name)
        compress_file(file_name)
        logger.info("cycle over fetched Disk metrics")
        Timer(5, disk_entity).start()   
    disk_entity()
fetch_du()