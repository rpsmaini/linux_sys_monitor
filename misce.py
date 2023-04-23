"""This code snippet stores functions which are commonly used in other codes
it includes timestamp function, Bytes to Mbytes/Gbytes converter and
directory creation function."""

import gzip
import os
import time
from datetime import datetime
from getmac import get_mac_address as gma
import logging
import gzip

#this function generate timestamp
def get_timestamp():
    timestamp = time.time()
    dt_obj = datetime.fromtimestamp(timestamp)
    return dt_obj.strftime("%d-%m-%y %H:%M:%S")

#this function converts Bytes into MB/GB   
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#this function will create directories and sub folder structure

def initializer():
    # directory creation
    mac = str(gma())
    serial = mac.replace(":","")
    usr = str(os.getlogin()+"_"+serial)#naming for user directory 
    directory = "dnw_monitoring"#parent directory

    # Parent Directory path
    parent_dir = "/home"#location where parent directory will be created
    # mode
    mode = 0o777         
    d_path = os.path.join(parent_dir, directory)
    d_path = os.path.join(d_path, usr)
    #print("the path is" + d_path)
        
    #FileExistsError exceptation handling
    try:
        os.makedirs(d_path,mode,exist_ok=True)
        #print("Directory '%s' created" %directory)
    except FileExistsError:
        print("File exists in :"+ d_path) 
    #print(d_path)    #debugging 
    util_path = os.path.join(d_path, 'utils/')
    os.makedirs(util_path, mode, exist_ok=True)
    rel_upath = os.path.relpath(util_path)
    #print("path for util folder :" + rel_upath)

    date_path = os.path.join(d_path, 'date/')
    #os.makedirs(date_path, mode, exist_ok=True)
    rel_dpath = os.path.relpath(date_path)
    #print("path for date folder :" + rel_dpath)

    report_path = os.path.join(d_path, 'report/')
    os.makedirs(report_path, mode, exist_ok=True)
    rel_rpath = os.path.relpath(report_path)
    #print("path for date folder :" + rel_dpath)
    return date_path, util_path, report_path, rel_dpath, rel_upath,d_path

def compress_file(filename):
    file= open(filename, 'rb')
    data = file.read()
    bindata = bytearray(data)
    with gzip.open(str(filename)+".gz", "wb") as f:
        f.write(bindata)

def send_datefile():
     pass

dirs = initializer()
logging.basicConfig(filename=os.path.join(dirs[1], "log.txt"), level=logging.DEBUG,format="%(levelname)s: %(asctime)s: %(message)s",filemode= 'a')
logger = logging.getLogger()
