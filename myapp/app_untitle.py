#urs/bin/python
#coding:utf8
import unittest,time
from appium import webdriver

class MyTestCase(unittest.TestCase):
    #脚本初始化，获取操作实例
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']=''#指定平台
        desired_caps['platformVersion']=''#和Appium里设置的一样
        desired_caps['deviceName']=''#指定需要控制的设备，在控制台中输入adb devices 就会出现deviceName
        desired_caps['appPackage']=''#被测试程序的packageName，在控制台中输入adb logcat | grep(findstr) START
        desired_caps['appActivity']=''#packageName中/后面的就是这个
        desired_caps['unicodeKeyboard']='True'#更改测试机的输入法
        desired_caps['resetKeyboard']='True'#将更改后的输入法还原为机器原来的输入法，值为false则不还原
        #获得操作程序的句柄，用Remote实现
        #4723可以在启动APPium时，看到
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        
    #释放实例，释放资源
    def tearDown(self):
        self.driver.quit()
        
    #测试的脚本
    def test_Add(self):
        #判断APP是否安装了
        print self.driver.is_app_installed('com.example.zhangjian.minibrowser2')#参数：APP包名
        #删除APP
        self.driver.remove_app('com.example.zhangjian.minibrowser2')#参数：APP包名
        #安装APP，（会遇到一个问题，初始化时由于没有这个APP会报错，可以修改初始化时的APP，然后这里的语句再安装我们想要安装的APP）
        self.driver.install_app('Users/zhangjiang/Downloads/app-debug.apk')#参数：APP在当前系统下的路径
        #启动APP
        self.driver.launch_app()
        time.sleep(3)
        
        #关闭APP
        self.driver.close_app()
        self.driver.launch_app()
        #启动activity
        self.driver.start_activity('com.example.zhangjian.minibrowser2','.myapplication.NewActivity')#参数1：包名，参数2：activity名
        #截屏
        time.sleep(3)
        self.driver.get_screenshot_as_file('test.png') # 图片保存在当前脚本目录下
        time.sleep(5)
        
        #快速滑动 API flick的用法
        self.driver.flick(100,750,100,100)
        #当前activity API current_Activity的用法
        print self.driver.current_activity
        #将某一个APP置于后台，3s钟后再调回前台
        self.driver.background_app(3)
        #等待指定activity显示API wait_activity的用法
        print self.driver.wait_activity('activity名称',3,1)# 3表示等待3秒，1表示1秒中check一下activity是否显示了
    
        #Locate定位一个元素,Operate操作一个元素
        self.driver.find_element_by_id('digit8').click()
        self.driver.find_element_by_id('plus').click()
        self.driver.find_element_by_id('digit5').click()
        self.driver.find_element_by_id('equal').click()
        #Verify验证结果
        #获取计算结果，结果处无id，使用class定位元素
        try:
            value=self.driver.find_element_by_class_name('android.widget.EditText').text
            self.assertEqual('13',value)
        except Exception:
            print u'出现异常了'
            self.fail(u'程序出现异常')
        #Exception异常处理的情况
        
    def testOtherAPI(self):
        '''
        elements=self.driver.find_elements_by_id("digit8")
        elements[0].click()
        time.sleep(3)
        print len(elements)'''
        
        # find_element_by_accessibility_id 的用法
        self.driver.find_element_by_id('digit1').click()
        self.driver.find_element_by_id('digit0').click()
        # accessibility 定位取content-desc的属性值
        self.driver.find_element_by_accessibility_id(u"除").click()# 点击“除号”
        
        self.driver.find_element_by_id("equal").click()
        time.sleep(3)
        
    def test_moreAPI(self):
        #获取元素列表
        els=self.driver.find_elements_by_class_name("")
        '''
        # 1.滚动scroll的用法
        # 指定从某个元素滚动到另一个元素的位置
        self.driver.scroll(els[10],els[1])
        # 2.拖拽drag_and_drop的用法
        # 选中某个元素拖拽到另一个元素的位置
        self.driver.drag_and_drop(els[10],els[3])
        # 3.滑动swipe的用法
        # 需要传入4个参数（start_x,start_y,end_x,end_y）
        self.driver.swipe(100,750,100,100)
        # 4.点击tap的用法
        # 参数传入坐标点
        self.driver.tap([(100,750)])
        '''
        # 1.快速滑动flick的用法
        self.driver.flick(100,750,100,100)
        # 2.显示当前activity的api current_activity的用法
        print self.driver.current_activity
        # 3.将某一个app置于后台，3s后再调回前台
        self.driver.background_app(3)
        # 4.等待指定activity显示API
        print self.driver.wait_activity('activity名称',3,1)# 3表示等待3秒，1表示1秒中check一下activity是否显示了
        
if __name__=='__main__':
    unittest.main()
