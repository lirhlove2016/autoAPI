# -*- coding: utf-8 -*-
import subprocess
import time
import os

class TimeoutError(Exception):
    pass

def excuteCmd(cmd, timeout=1):
    # src = raw_input(unicode("请输入源文件完整路径及文件名： ", 'utf-8').encode('gbk'))
    # dst = raw_input(unicode("请输入目标文件完整路径及文件名： ",'utf-8').encode('gbk'))
    # cmd = 'copy "%s" "%s"'%(src,dst)
    s = subprocess.Popen(cmd, shell=True)
    beginTime = time.time()
    secondsPass = 0
    while True:
        if s.poll() is not None:
            break
        secondsPass = time.time() - beginTime
        if timeout and timeout < secondsPass:
            s.terminate()
            print(u"超时!")
            return False
        time.sleep(0.1)
    return True

# main function
if __name__ == '__main__':
    ''' self test '''
    cmd="adb devices"
    ret= os.system(cmd)
    print(ret)
    ret2= os.popen(cmd)
    print('ret2---------',ret2)

    print('call-------------------')
    ret=subprocess.call(cmd)
    print('ret=',ret)

    print('getoutput----------------------')
    ret=subprocess.getoutput(cmd)
    print(ret)

    print('---popen')
    os.popen(cmd).read()


    '''
    try:
        print("test1")
        ret = excuteCmd("echo start && ping -n 2 127.0.0.1 > nul && echo done ",5)
        print(ret)
        print("test2")
        ret = excuteCmd("adb devices ",5)
        print(ret)
    except TimeoutError as e:
        print(repr(e))
	'''