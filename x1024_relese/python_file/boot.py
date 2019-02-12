# This file start network and ftp serve

import network
import time

my_ssid = 'my_ssid'
my_passwd = 'my_passwd'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(my_ssid,my_passwd)

time.sleep(5)
sta.ifconfig()

network.ftp.start(user = 'xilinx',password = 'xilinx',buffsize = 1024,timeout = 300)
print("IP of this X1024 is : " + sta.ifconfig()[0])
