from selenium import webdriver

mobile_emulation = {'deviceName':'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',mobile_emulation)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.implicitly_wait(30)



qiandao_url='http://192.168.0.10:3080/asg/portal/sign/signlist.do?v=1&json={"pub":{"deviceId":"dz13c7f29f08eb4114aed54a5bd83e778e","subPline":"2","screen":"1080x1920","appCode":"ishugui","dzPaySupport":"2","userId":"5163","apiVersion":"3.8.4.2051","pname":"com.ishugui","channelCode":"Google","os":"android23","v":"1","imei":"352107063628066","p":"33","brand":"samsung","clientAgent":"svnVer_1811061002","version":"3.8.4.2051","apn":"wifi","macAddr":"84:38:38:7E:EC:D8","imsi":"","channelFee":"Google","model":"SM-G9008V"},"pri":{"app_scheme":"ishugui","isLogin":"2","phoneNum":"","sex":"0","app_host":"calander_web","shareSupport":"2","maxAward":"20"}}'
driver.get(qiandao_url)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='补签'])[2]/following::li[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[1]").click()


driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='补签'])[25]/following::em[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即领取'])[1]/following::span[1]").click()
driver.find_element_by_link_text(u"上期中奖名单").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日常任务'])[1]/following::li[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='去完成'])[5]/following::a[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='已领取'])[1]/following::span[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='我知道了'])[1]/following::li[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='去完成'])[1]/following::a[1]").click()
driver.find_element_by_link_text(u"朕知道了").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上期中奖名单'])[1]/following::span[3]").click()
