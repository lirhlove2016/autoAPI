#coding=utf-8
import appium
from appium import webdriver
from yongli import *
import time

platformName("android")
print(desired_caps)

aaa= ""

driver = DRIVER()




DENGDAI()

# sx = SIZE()[0]
# sy = SIZE()[1]
# ex = SIZE()[2]
# ey = SIZE()[3]
# print(sx,sy,ex,ey)

START()
START()
NAN()
time.sleep(1)
SHUCHENG()
time.sleep(3)
UP()
time.sleep(3)
print(driver.contexts)
LEFT()
time.sleep(3)
print(driver.contexts)
LEFT()
time.sleep(3)
print(driver.contexts)
RIGHT()
time.sleep(1)
print(driver.contexts)
FENLEI()
time.sleep(2)
DOWN()
time.sleep(2)
WODE()
time.sleep(2)
DOWN()
time.sleep(2)
UP()
time.sleep(2)
SHUJIA()
time.sleep(2)
RC()
time.sleep(3)


print(driver.contexts)





# el1 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el1.click()
# el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
# el3.click()
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
# el4.click()
# el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]")
# el5.click()
# el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]")
# el6.click()
# el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]")
# el7.click()








driver.quit()
