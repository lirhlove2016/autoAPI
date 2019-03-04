import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

from time import sleep
#import uiautomator2 as u2

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import readexcel as reader, writeexcel as writer
from common import elementApp as app


"""
1.toast提示判断，is_toast_exist(driver, "看到的内容")
2.权限弹窗，always_allow(driver,number=判断次数)


"""

# 写入结果
def wirte_result(result, value):
    if reader.rr>0:
        writer.write(reader.rr - 1, 7, result)
        writer.write(reader.rr - 1, 8, value)

#-----------------------------------------------------------------
def is_toast_exist1(driver,text,timeout=20,poll_frequency=0.5):
    '''is toast exist, return True or False
    - driver - 传driver
    - text - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency - 间隔查询时间，默认0.5s查询一次
    :Usage:
    is_toast_exist(driver, "看到的内容")
    '''
    print('提示信息-----------------',text)
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        #print(toast_loc)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        re='PASS'
        print('T--------------------------')
        wirte_result(re,text)
        
        return True
    except:
        
        re='FAIL'
        print('F--------------------------')
        wirte_result(re,text)
        
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
        except Exception as e:
            print('error:',text)
            return False

#-----------------------------------------------------------------
def is_toast_exist(driver,text,act="",element="",timeout=10,poll_frequency=0.5):
    print('toast-----------------',text,act)

    #先进行元素操作
    if act in ["id","name","xpath"]:
        print("执行操作---------------------",act)
        app.get_elements(act,element)
        app.e.click()

    elif act=="back":
        #print('执行操作--------------------',act)
        app.back()
        
    else:
        print('直接判断')

    #再进行判断      
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        #print(toast_loc)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        re='PASS'
        print(re)
        wirte_result(re,text)
        
        return True
    except :
        
        re='FAIL'
        print(re)
        wirte_result(re,text)
        
        return False


        
if __name__== "__main__":
    #pass

    desired_caps = {
            'platformName': 'Android',
            'deviceName': '6EB0217518004226',
            'platformVersion': '6.0',
            'appPackage': 'com.ishugui',
            'appActivity': 'com.dzbook.activity.LogoActivity',
            'noReset': 'true',
            #'automationName': 'uiautomator2',
    }
    print("连接中。。。。。。")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print("连接成功")

    sleep(5)
    driver.back() # 点返回

    # 判断是否存在toast-'再按一次退出'
    print(is_toast_exist1(driver, "再按一次退出"))
    sleep(5)
    driver.back() # 点返回
    print(is_toast_exist1(driver, "再按一次退出"))

	
