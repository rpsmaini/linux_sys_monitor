"""This code function uploads file to django server """
from fileinput import filename
import os
import requests
from misce import*
from threading import Timer
test_url = "http://192.168.1.117:8000/compare_Context"#to be replaced by django svr url
 
dirs = initializer()

def file_upload():
    #let it be folder with files to upload
    folder = dirs[1]
    files = [('log_txt', open(os.path.join(dirs[1],'/log.txt'), 'rb')), #replace static path with 
    ('cpu_insights', open(os.path.join(dirs[1],'/cpu_insights.csv', 'rb'))),# dynamic path
    ('ram_insights', open(os.path.join(dirs[1],'/ram_insights.csv', 'rb'))),
    ('network_insights', open(os.path.join(dirs[1],'/network_insights.csv', 'rb'))),
    ('disk_insights', open(os.path.join(dirs[1],'/disk_insights.csv', 'rb'))),
    ('process_log', open(os.path.join(dirs[1],'/process_log.csv', 'rb'))),
    ('system_json', open(os.path.join(dirs[1],'/system.json', 'rb'))),
]   
    r=requests.post(test_url, files=files)
    r.text
    print("upload Done")
file_upload()    