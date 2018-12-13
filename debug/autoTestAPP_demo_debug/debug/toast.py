import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

from time import sleep
#import uiautomator2 as u2

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
        'platformName': 'Android',
        'deviceName': '6EB0217518004226',
        'platformVersion': '8.0',
        'appPackage': 'com.ishugui',
        'appActivity': 'com.dzbook.activity.LogoActivity',
        'noReset': 'true',
        'automationName': 'uiautomator2',
}

def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
    '''is toast exist, return True or False
    :Agrs:
    - driver - 传driver
    - text - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency - 间隔查询时间，默认0.5s查询一次
    :Usage:
    is_toast_exist(driver, "看到的内容")
    '''

    #d = u2.connect_usb('6EB0217518004226')
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        print(toast_loc)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False

if __name__== "__main__":

    print("连接中。。。。。。")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print("连接成功")
    # 等主页面activity出现
    #driver.wait_activity(".base.ui.MainActivity", 10)

    sleep(5)

    driver.back() # 点返回

    # 判断是否存在toast-'再按一次退出'
    print(is_toast_exist(driver, "再按一次退出"))
    sleep(5)
    driver.back() # 点返回
    print(is_toast_exist(driver, "再按一次退出"))