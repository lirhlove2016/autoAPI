#coding:utf-8


#底部菜单
bottom_menu=["com.ishugui:id/imageView","com.ishugui:id/textView","com.ishugui:id/bottomBarLayout","书架","书城","分类","我的"]
bottom_id=["com.ishugui:id/imageView","com.ishugui:id/textView","com.ishugui:id/bottomBarLayout"]
battom_name=["书架","书城","分类","我的"]

#不点击的元素
Notclick_name=['电话','联系客服','立即充值','立即开通','立即续费','支付']
#点击的元素
click_name=['永久允许','确定','取消']
#弹窗关闭
tanchuang_close_id=["com.ishugui:id/imageview_close","com.ishugui:id/imageview_cloud_sysch_close"]

#设备参数
desired_caps = {
    'platformName': 'Android',
    'deviceName':'T8B6W4LJU4VSQWWW', #6EB0217518004226  
    'platformVersion': '6.0',
    #'app': PATH(r'E:\download\389.apk'), #安装目录
    'appPackage': 'com.ishugui',  
    'appActivity': 'com.dzbook.activity.LogoActivity',
}