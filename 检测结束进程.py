import os
import win32api
# process_name:进程名 ；返回进程个数
def process_exit(process_name):
    p_checkresp = os.popen('tasklist /fo csv | find "' + process_name + '"').readlines()
    return len(p_checkresp)


if process_exit('TIM.exe')== 0:    # 未检测到
    print("=0")
elif process_exit('TIM.exe') >= 1:    # 检测到
    command = 'taskkill /F /IM TIM.exe'  # kill
    os.popen(command)    # 执行cmd命令
    # os.system(command)    # 听说用popen更好
    print("=1")
else:
    win32api.MessageBox(0, "用api弹出窗口消息")