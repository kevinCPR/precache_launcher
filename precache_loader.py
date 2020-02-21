import os
from os.path import expanduser
home = expanduser("~")
with open(home,'/precache/precache_launcher/Apple_mobile_device_types.txt') as f:
    mobileDevices = f.read().splitlines()

i = 1

for i in mobileDevices:
    if i == '':
        continue
    model = i.split(':')[0]
    friendlyName = i.split(':')[1][1:]
    if "iPhone" in model:
        command = "~/precache/precache/precache.py -cs http://localhost:49269 -i " + model + " -o home/precache/IPSWs/iPhone/"
    if "iPod" in model:
        command = "~/precache/precache/precache.py -cs http://localhost:49269 -i " + model + " -o home/precache/IPSWs/iPod/"
    if "iPad" in model:
        command = "~/precache/precache/precache.py -cs http://localhost:49269 -i " + model + " -o home/precache/IPSWs/iPad/"
    if "Watch" in model:
        command = "~/precache/precache/precache.py -cs http://localhost:49269 -i " + model + " -o home/precache/IPSWs/Watch/"
    print(friendlyName)
    os.system(command)
