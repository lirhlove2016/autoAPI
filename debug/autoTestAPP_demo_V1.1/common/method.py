#coding:utf-8
import time,os
"""
1.is_exist  判断元素是否存在
2.backs    返回多次操作

"""
close_ids=[]


#单个元素，判断是否存在，若存在则点击操作
def is_exist(driver,act,value,*args):
        global driver
        print('正在判断元素是否存在--------------',act,value)
        el=""
        try:

                if act=="id":
                        el=driver.find_element_by_id(value)
                        
                elif act=="name":
                        el=driver.find_element_by_name(value)
                elif act=="xpath":
                        el=driver.find_element_by_xpath(value)

                el.click()

        except Exception as err:
            
            print('报错是----',err)
            print('元素不存在！')



#多次返回操作
def backs(driver,number=1,*args):
        global driver
        for i in range(len(number)):
                driver.back()
                                
