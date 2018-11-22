#coding: utf-8
from selenium import webdriver
from time import sleep
'''
mobile_emulation = {'deviceName':'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',mobile_emulation)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get("http://www.baidu.com")

'''

#指定了宽度、高度、分辨率以及ua标识
WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0

UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
#mobileEmulation = {"deviceName":"iPhone X"}
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('http://m.baidu.com')

driver.maximize_window()

sleep(3)
print("正在退出....")
#driver.close()
driver.quit()
