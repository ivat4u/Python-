# -*- coding: UTF-8 -*-
import win32api
import win32con

def LeftClick(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
    win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 测试

def PressOnce(x):    # 模拟键盘输入一个按键的值，键码: x
    win32api.keybd_event(x, 0, 0, 0)
'''  键盘键与虚拟键码对照表
　　　 　　字母和数字键 数字小键盘的键功能键 其它键 
　　　　　　键　　 键码　  　键　　 键码　　　 键　　 键码 　　  键　　　　键码 
　　　　　　A　　　65　　   0 　　96 　　　　F1 　　112 　　Backspace 　　　8 
　　　　　　B　　　66　　   1　　 97 　　　　F2 　　113　　 Tab 　　　　　　9 
　　　　　　C　　　67 　　  2 　　98 　  　　F3 　　114　　  Clear 　　　　　12 
　　　　　　D　　　68　　　3　　 99 　　　　F4 　　115　　Enter 　　　　　13 
　　　　　　E　　　69 　　  4 　　100　　　　F5 　　116　　Shift　　　　　 16 
　　　　　　F　　　70 　　  5 　　101　　　　F6 　　117　　Control 　　　　17 
　　　　　　G　　　71 　　  6　　 102　　　　F7 　　118 　　Alt 　　　　　　18 
　　　　　　H　　　72 　　　7 　　103　 　　F8 　　119　　Caps Lock 　　　20 
　　　　　　I　　　73 　　　8 　　104　　　　F9 　　120　　Esc 　　　　　　27 
　　　　　　J　　　74 　　　9　　 105　　　　F10　　121　　Spacebar　　　　32 
　　　　　　K　　　75 　　　* 　　106　  　　F11　　122　　Page Up　　　　 33 
　　　　　　L　　　76 　　　+ 　　107　　  　F12　　123　　Page Down 　　　34 
　　　　　　M　　　77 　　　Enter 108　　　　-- 　　--　　　End 　　　　　　35 
　　　　　　N　　　78 　　　-　　 109　　　　-- 　　-- 　　　Home　　　　　　36 
　　　　　　O　　　79 　　　. 　　110　　　　--　　 -- 　　 　Left Arrow　　　37 
　　　　　　P　　　80 　　　/ 　　111　　　　--　　 -- 　　 　Up Arrow　　　　38 
　　　　　　Q　　　81 　　　-- 　　--　　　 　--　　 -- 　　 　Right Arrow 　　39 
　　　　　　R　　　82 　　　-- 　　--　　　　--　　 -- 　　 　　Down Arrow 　　 40 
　　　　　　S　　　83 　　　-- 　　--　　　　　-- 　　-- 　　 　Insert 　　　　 45 
　　　　　　T　　　84 　　　-- 　　--　　　　　--　　 -- 　　 　Delete 　　　　 46 
　　　　　　U　　　85 　　　-- 　　--　　　 　-- 　　-- 　　 　Help 　　　　　 47 
　　　　　　V　　　86 　　　--　　 --　　　　-- 　　-- 　　 　Num Lock 　　　 144 
　　　　　　W　　　87 　　　　　　　　　
　　　　　　X　　　88 　　　　　
　　　　　　Y　　　89 　　　　　
　　　　　　Z　　　90 　　　　　
　　　　　　0　　　48 　　　　　
　　　　　　1　　　49 　　　　　
　　　　　　2　　　50 　　　　　　
　　　　　　3　　　51 　　　　　　
　　　　　　4　　　52 　　　　　　
　　　　　　5　　　53 　　　　　　
　　　　　　6　　　54 　　　　　　
　　　　　　7　　　55 　　　　　　
　　　　　　8　　　56 　　　　　　
　　　　　　9　　　57 　'''
# 测试
LeftClick(30, 30)  # 我的电脑？
PressOnce(13)  # Enter
PressOnce(9)   # TAB