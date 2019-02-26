# coding:utf-8
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

from time import sleep
#import uiautomator2 as u2

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
1.toast提示判断，is_toast_exist(driver, "看到的内容")
2.权限弹窗，always_allow(driver,number=判断次数)

"""

#-----------------------------------------------------------------
def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
    '''is toast exist, return True or False
    - driver - 传driver
    - text - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency - 间隔查询时间，默认0.5s查询一次
    :Usage:
    is_toast_exist(driver, "看到的内容"
    '''
    if type(timeout)=='str':
        timeout=int(timeout)
    elif type(poll_frequency)=='str':
        poll_frequency=int(poll_frequency)
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        print(toast_loc)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False

#-----------------------------------------------------------------
#权限允许弹窗，判断弹窗次数，默认5次，0.5s判断一次
def always_allow(driver,number=5):
    '''is always allow exist, return True or False
    - driver - 传driver
    - number - 判断次数，默认5次
    - poll_frequency - 间隔查询时间，默认0.5s查询一次
    :Usage:
    always_allow(driver,number=判断次数)
    '''
    for i in range(number):
        loc=("xpath", ".//*[contains(@text,'%s')]"%text)
        try:
            e=WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
            e.click()
            return True
        except as e:
            print('error:',e)
            return False

        
if __name__== "__main__":

    print("连接中。。。。。。")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print("连接成功")
    sleep(5)
    driver.back() # 点返回
    # 判断是否存在toast-'再按一次退出'
    print(is_toast_exist(driver, "再按一次退出"))
    sleep(5)
    driver.back() # 点返回
    print(is_toast_exist(driver, "再按一次退出"))
	
	
