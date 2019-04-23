# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


#设置使用浏览器
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#最大化窗口
driver.maximize_window()
#输入搜索内容
driver.find_element_by_id("kw").send_keys("selenium")

#点击搜索
driver.find_element_by_id("su").click()

#查询是否有

time.sleep(5)
driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
#关闭浏览器
print('正在退出浏览器...')
driver.quit()


