# MicroPython for X1024 Alpha

## 1.使用uPyCraft将micropython_x1024_alpha.bin烧录到ESP32上

* uPyCraft 下载地址：https://gitee.com/dfrobot/upycraft/
* uPyCraft 使用说明：http://docs.dfrobot.com.cn/upycraft/

## 2.加载Python文件

由于固件尚处于开发阶段，没有把xfpga库编译到固件中，需要用uPyCraft将python_file中的xfpga.py传到ESP32上。
.bit文件使用串口传输太慢，所以使用ftp服务器，boot.py文件中已经配置好，只需要把
```Python
my_ssid = 'my_ssid'
my_passwd = 'my_passwd'
```
替换成你的wifi ssid和密码

## 3.使用ftp连接ftp服务器，并发送.bit文件

ftp服务器的使用见https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/ftpserver

User:xlinx Password:xlinx，注意需要把.bit文件加载到/flash/overlay/ 文件夹下。

## 4.配置FPGA
你可以在Python shell 中输入
```python
import xfpga
xfpga.overlay('xxx.bit')
```
把xxx.bit加载到Xilinx FPGA上。

如果你想让ESP32上电配置FPGA，可以把这段程序写进main.py中。

