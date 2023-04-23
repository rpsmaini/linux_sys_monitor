"""This code snippet shows gpu utilization using 
GPUtil module which only fetches nvdia based gpu 
to be considered in scope for improvement"""
from misce import*
import GPUtil
from threading import Timer
import pandas as pd
import logging
global df
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger() 
df = pd.DataFrame(columns= ['Id', 'Gpu Name', 'GPU load', 'GPU free memory', 'GPU used memory', 'GPU total memory', 'GPU Temperature', 'GPU UUID', 'timestamp'])
file_name = os.path.join(dirs[1], "gpu_usage.csv")
def gpu_insights():
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        gpu_dict={gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid, get_timestamp()}
        list_gpus.append(gpu_dict)
    df = pd.DataFrame(list_gpus)
    df.to_csv(file_name)
    compress_file(file_name)
    Timer(5, gpu_insights).start()
gpu_insights()