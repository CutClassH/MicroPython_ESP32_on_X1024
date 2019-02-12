#   File:     main.py
#   Description : None
#   Copyright (c) 2019, X1024.
#   All rights reserved.

import xfpga
import time

start = time.ticks_ms()
xfpga.overlay('test.bit')
print(time.ticks_ms()-start)
