#coding:utf-8
from appium import webdriver
import time,os



#获取屏幕宽度和高度
def getSize():
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x, y)

#向左滑动
def swipeLeft():
	s= getSize()
	x1 = int(s[0] * 0.9)
	y1 = int(s[1] * 0.5)
	x2 = int(s[0] * 0.1)
	driver.swipe(x1, y1, x2, y1)

#使用设备配置
desired_caps ={
  "platformName": "Android",
  "deviceName": "722347d6",
  "platformVersion": "6.0",
  "appPackage": "com.ishugui",
  "appActivity": "com.dzbook.activity.LogoActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
print('Start-------------------------------------------------')


#启动页向左滑动
i=0
while i <3:
    swipeLeft()
    i=i+1

time.sleep(5)
#选择男
driver.find_element_by_id("com.ishugui:id/tv_man").click()

#关闭弹窗   
el2 = driver.find_element_by_id("com.ishugui:id/imageview_cloud_sysch_close")
el2.click()

#我的 
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]")
el3.click()
#书架
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
el4.click()
#点击书架-搜索
el5 = driver.find_element_by_id("com.ishugui:id/iv_top_title_search")
el5.click()
#输入搜索内容
el8 = driver.find_element_by_id("com.ishugui:id/edit_search")
el8.send_keys("123")
#点击搜索
el9 = driver.find_element_by_id("com.ishugui:id/textview_search")
el9.click()
#返回
el10 = driver.find_element_by_id("com.ishugui:id/imageview_back")
el10.click()
el11 = driver.find_element_by_id("com.ishugui:id/imageview_back")
el11.click()

#
el12 = driver.find_element_by_id("com.ishugui:id/tv_sign_status")
el12.click()
#书架-进入签到
el13 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.TextView")
el13.click()

#点击签到-第一次进入
#el14 = driver.find_element_by_xpath("//android.view.View[@content-desc=\"签到\"]")
#el14.click()
#展示日历

time.sleep(5)

el15 = driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"签到\"]/android.view.View[3]")
el15.click()
#收起日历
el16 = driver.find_element_by_xpath("//android.webkit.WebView[@content-desc=\"签到\"]/android.view.View[3]")
el16.click()
#返回
el17 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView")
el17.click()
print('End----------------------------------------------------')
