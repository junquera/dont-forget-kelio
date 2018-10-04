# https://pyudev.readthedocs.io/
import pyudev
import requests
import simplejson as json
from datetime import datetime

context = pyudev.Context()

monitor = pyudev.Monitor.from_netlink(context)

print("Insert device")

d = None

for device in iter(monitor.poll, None):
    try:
        # Si no tiene DEVNAME, puede ser algo "virtual"
        # if ('DEVNAME' in device and 'ID_VENDOR_ID' in device and 'ID_MODEL_ID' in device) or ('DEVNAME' in device and device.action not in ['add', 'bind']):
        if 'BUSNUM' in device and device.action == 'add':
            id_device = "%s %s" % (device.get('ID_VENDOR'), device.get('ID_MODEL'))
            id_device_id = "%s %s" % (device.get('ID_VENDOR_ID'), device.get('ID_MODEL_ID'))
            ok = input("%s (%s). Ok? (y/N) " % (id_device, id_device_id))
            if ok[0].lower() == 'y':
                d = device.get('BUSNUM')
                break
    except Exception as e:
        pass

from subprocess import call

for device in iter(monitor.poll, None):
    if 'BUSNUM' in device:
        if device.get('BUSNUM') == d and device.action == 'add':
            call(['/home/junquera/desficha/ficha.sh'])
        if device.get('BUSNUM') == d and device.action == 'remove':
            call(['/home/junquera/desficha/desficha.sh'])
