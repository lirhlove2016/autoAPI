#coding=utf-8
from selenium import webdriver
import os
import time
# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop = 2

# 默认广告条数
ads_num_require = 8
# 请求连接
req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"
# 打开浏览器

browser = webdriver.Chrome()
#rowser = webdriver.Firefox()
# 开始请求
browser.get(req_url)
# 获取所有的广告

all_ads_li = browser.find_elements_by_css_selector('#e_idea_pp li')
# 当前广告条数
ads_num_current = len(all_ads_li)
print("Has been got %d ads" %(ads_num_current))
# 如果广告条数与默认不符
if ads_num_current < ads_num_require:
    print("The number of ads is not enough ( current : %d require: %d)" %(ads_num_current,ads_num_require))
    # exit()


