# coding:utf-8
from appium import webdriver
from time import sleep

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'T8B6W4LJU4VSQWWW',#127.0.0.1:62001
                'platformVersion': '6.0',
                'appPackage': 'com.ishugui',
                'appActivity': 'com.dzbook.activity.LogoActivity',
                #'noReset': 'true',
                #'resetKeyboard': 'true',
                #'unicodeKeyboard': 'true'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
driver.wait_activity(".com.dzbook.activity.LogoActivity", 10)
#进入主界面

#定位-书架-签到
e=driver.find_element_by_id("com.ishugui:id/tv_sign_status")
# 获取text
t1 = e.text
print("获取text",t1)

# 获取tag_name
t2 = e.tag_name
print(t2)

# content-desc为空，获取的是text
t3 = e.get_attribute("name")
print(t3)

# content-desc
t4 = e.get_attribute("name")
print(t4)

# id
t5 = e.get_attribute("resourceId")
print(t5)

# class
t6 = e.get_attribute("className")
print(t6)

# text
t7 = e.get_attribute("text")
print(t7)

# checkable
t8 = e.get_attribute("checkable")
print(t8)

# clickable
t9 = e.get_attribute("clickable")
print(t9)

# size
t10 = e.size
print(t10)

# location
t11 = e.location
print(t11)

