import os
import re
import subprocess
import time

response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)
print("TestSuccessfull")
##ping[0] = ping[0].replace(',', '.')
##download[0] = download[0].replace(',', '.')
##upload[0] = upload[0].replace(',', '.')
#if os.stat('/Users/hiramknick/code/personal/PythonSpeedTest/results/sample.csv').st_size == 0:
print('Date,Time,Ping,Download,Upload')
print('{},{},{},{},{}'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping[0], download[0], upload[0]))
