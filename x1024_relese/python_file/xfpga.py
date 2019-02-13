#   Module:     xfpga
#   Description: the funtions for X1024 board.
#   [https://github.com/PYNQ-X1024/MicroPython_ESP32_on_X1024]
#   Copyright (c) 2019, X1024 Project.
#   All rights reserved.

__auther__ = 'CCHs,SWJTU'


import os
import time
from micropython import const
from machine import SPI, Pin


XFPGA_MODEL = '7s15ftgb196'

_XFPGA_CCLK_PIN = const(22)
_XFPGA_DIN_PIN = const(23)
_XFPGA_PROGRAM_PIN = const(19)
_XFPGA_INTB_PIN = const(18)
_XFPGA_DONE_PIN = const(5)


def bitstream_check(file_name):
    '''
    Check if the file is bitstream fil.
    :param file_name:
    :return: success:overlay_path ,fail:None
    '''

    rootdir_list = os.listdir('/')
    overlay_list = os.listdir('/flash/overlay')
    if file_name  in overlay_list:
        overlay_path = '/flash/overlay/'
    elif 'sd' in rootdir_list:
        overlay_list = os.listdir('/sd/overlay')
        if file_name  in overlay_list:
            overlay_path = '/sd/overlay/'
        else:
            print('"' + file_name + '" does not exist in overlay folder.')
            return None
    else:
        print('"'+file_name +'" does not exist in overlay folder.')
        return None

    if file_name.endswith('.bit') or file_name.endswith('.bit'):
        return overlay_path
    else:
        print('"'+file_name +'" is wrong file type.')
        return None



def overlay(file_name):
    '''
    Load the bitsteam file into the FPGA with serial configuration.
    :param file_name:
    :return: None
    '''

    overlay_path = bitstream_check(file_name)
    if  overlay_path == None:
        raise ValueError('Wrong File')

    # Soft SPI for serial output
    xfpga_spi = SPI(2,baudrate=20000000,  polarity=0, phase=0,firstbit =SPI.MSB,\
                    sck=Pin(_XFPGA_CCLK_PIN), mosi=Pin(_XFPGA_DIN_PIN),miso=Pin(_XFPGA_DONE_PIN))

    #GPIO Initialize
    xfpga_intb = Pin(_XFPGA_INTB_PIN,mode = Pin.OUT_OD,pull=Pin.PULL_UP,value = 1)
    xfpga_program = Pin(_XFPGA_PROGRAM_PIN,mode=Pin.OUT,value=1)

    #FPGA configuration start sign
    xfpga_program.value(0)
    xfpga_intb.value(0)
    xfpga_program.value(1)
    xfpga_intb.value(1)

    #Sent Serial Configuration Data
    f = open(overlay_path + file_name,'rb')
    if file_name.endswith('.bit') :
        f.seek(100,0)
    while True:
        f_byte = f.read(1)
        if len(f_byte)==0 :
            break
        xfpga_spi.write(f_byte)
    f.close()
    xfpga_spi.deinit()

    xfpga_done = Pin(_XFPGA_DONE_PIN, mode=Pin.IN, pull=Pin.PULL_UP)

    if xfpga_done.value() == 0:
        raise ConnectionError('FPGA Configuration Failed')






