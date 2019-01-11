# -*- coding: UTF-8 -*-
import win32api
from win32api import GetSystemMetrics
def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)

a, b = DisplaySize()
print '分辨率的为'+str(a)+'*'+str(b)
import os,time
import pyautogui as pag
print "将鼠标放在位置上，可以显示x,y坐标"
try:
    while True:
            print "Press Ctrl-C to end"
            x,y = pag.position() #返回鼠标的坐标
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print posStr#打印坐标
            time.sleep(2)
            os.system('cls')#清楚屏幕
except  KeyboardInterrupt:
    print 'end....'

