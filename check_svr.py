# import module
"""This code just checks if server is up and running
If server is up and running it will invoke file_upload function and will upload files"""
from urllib.request import urlopen
from urllib.error import *
from file_uploader import *
# try block to read URL
try:
	html = urlopen("http://192.168.1.78:8000/compare_Context")#replace url with the current server url
	
except HTTPError as e:
	print("HTTP error", e)
	exit()
except URLError as e:
	print("Opps ! Page not found!", e)
	exit()
else:
	print('Yeah ! found ')
	file_upload()