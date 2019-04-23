# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
          #self.driver = webdriver.Chrome()

        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        #h5
        mobile_emulation = {'deviceName':'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation',mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://192.168.0.10:3080/asg/portal/sign/signlist.do?v=1&json={%22pub%22:{%22deviceId%22:%22dz13c7f29f08eb4114aed54a5bd83e778e%22,%22subPline%22:%222%22,%22screen%22:%221080x1920%22,%22appCode%22:%22ishugui%22,%22dzPaySupport%22:%222%22,%22userId%22:%225163%22,%22apiVersion%22:%223.8.4.2051%22,%22pname%22:%22com.ishugui%22,%22channelCode%22:%22Google%22,%22os%22:%22android23%22,%22v%22:%221%22,%22imei%22:%22352107063628066%22,%22p%22:%2233%22,%22brand%22:%22samsung%22,%22clientAgent%22:%22svnVer_1811061002%22,%22version%22:%223.8.4.2051%22,%22apn%22:%22wifi%22,%22macAddr%22:%2284:38:38:7E:EC:D8%22,%22imsi%22:%22%22,%22channelFee%22:%22Google%22,%22model%22:%22SM-G9008V%22},%22pri%22:{%22app_scheme%22:%22ishugui%22,%22isLogin%22:%222%22,%22phoneNum%22:%22%22,%22sex%22:%220%22,%22app_host%22:%22calander_web%22,%22shareSupport%22:%222%22,%22maxAward%22:%2220%22}}")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='补签'])[25]/following::em[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即领取'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='补签'])[14]/following::li[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()
        driver.find_element_by_link_text(u"去完成").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='已领取'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='去完成'])[1]/following::a[1]").click()
        driver.find_element_by_link_text(u"朕知道了").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日常任务'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='去完成'])[6]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='去完成'])[5]/following::a[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='已领取'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='成就任务'])[1]/following::li[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):

        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
