# https://pyudev.readthedocs.io/
import pyudev
import requests
import simplejson as json
from datetime import datetime

context = pyudev.Context()

monitor = pyudev.Monitor.from_netlink(context)

print("Insert device")

bus_num = None
device_id = None

for device in iter(monitor.poll, None):
    try:
        # Si no tiene DEVNAME, puede ser algo "virtual"
        # if ('DEVNAME' in device and 'ID_VENDOR_ID' in device and 'ID_MODEL_ID' in device) or ('DEVNAME' in device and device.action not in ['add', 'bind']):
        if 'BUSNUM' in device and device.action == 'add':
            id_device = "%s %s" % (device.get('ID_VENDOR'), device.get('ID_MODEL'))
            id_device_id = "%s %s" % (device.get('ID_VENDOR_ID'), device.get('ID_MODEL_ID'))
            ok = input("%s (%s). Ok? (y/N) " % (id_device, id_device_id))
            if ok[0].lower() == 'y':
                bus_num = device.get('BUSNUM')
                device_id = id_device_id
                break
    except Exception as e:
        pass

from subprocess import call
import os
for device in iter(monitor.poll, None):
    if 'BUSNUM' in device:
        id_device_id = "%s %s" % (device.get('ID_VENDOR_ID'), device.get('ID_MODEL_ID'))

        if device_id == id_device_id and device.action == 'add':
            bus_num = device.get('BUSNUM')
            call([os.path.abspath('.') + '/ficha.sh'])

        if device.get('BUSNUM') == bus_num and device.action == 'remove':
            call([os.path.abspath('.') + '/desficha.sh'])
