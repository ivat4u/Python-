# -*- coding: UTF-8 -*-
from ctypes import *
import time
user32 = windll.LoadLibrary('user32.dll')    # 加载动态链接库
user32.BlockInput(True)   # 锁
time.sleep(5)             # 你-1s
user32.BlockInput(False)  # 该解锁啦