# This file start network and ftp server

import os

os.mountsd()

import network
import time


my_ssid = 'CGK'
my_passwd = 'cgk123456'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(my_ssid,my_passwd)

time.sleep(5)
sta.ifconfig(('192.168.1.100','255.255.255.0','192.168.1.1','8.8.8.8'))

network.ftp.start(user = 'xilinx',password = 'xilinx',buffsize = 1024,timeout = 300)
print("IP of this X1024 is : " + sta.ifconfig()[0])
