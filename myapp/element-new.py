def findel(AAA):
        try:
            s1 = driver.find_element_by_android_uiautomator("text(\"%s\")" %AAA)
            s1.click()
            print("元素定位成功")
        except BaseException as e:
            print(e.args)
            print("元素定位失败")