#coding:utf-8
import os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

#设备参数
android_caps={}
android_caps['platformName']='Android'
android_caps['deviceName']='T8B6W4LJU4VSQWWW'
android_caps['platformVersion']='6.0'
android_caps['appPackage']= 'com.ishugui'
android_caps['appActivity']='com.dzbook.activity.LogoActivity'
android_caps['app']=PATH(r'E:\download\389.apk')

ios_caps={}

#--------------------------------------------------------
#xml文件目录
#clicks调用
filepath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
pageDir = os.path.join(filepath, 'report/pages/')
imageDir = os.path.join(filepath, 'report/image/')  #截图


#--------------------------------------------------------
#common调用
#source中排除的属性值，android:id/statusBarBackground顶部状态，id
exclude=["android.widget.FrameLayout"]
#可点的属性
include=["android.widget.TextView","android.widget.ImageView","android.widget.EditText"]

#自定义可点的
user_custom=[]


#跳转到其他应用，back返回
appPackages=["com.ishugui"]

#----------------------------------------
#click调用----------------
#配置执行，id,name,class

#--------------------------------------------------------
#底部菜单，

'''
#底部菜单
bottom_menu=["com.ishugui:id/imageView","com.ishugui:id/textView","com.ishugui:id/bottomBarLayout","书架","书城","分类","我的"]
bottom_id=["com.ishugui:id/imageView","com.ishugui:id/textView","com.ishugui:id/bottomBarLayout"]
battom_name=["书架","书城","分类","我的"]
tanchuang_closseid=["com.ishugui:id/imageview_close","com.ishugui:id/imageview_cloud_sysch_close"]
'''
#

package="com.aikan"
#clicks调用
bottom_menu=["%s:id/imageView"%package,"%s:id/textView"%package,"%s:id/bottomBarLayout"%package,"书架","书城","分类","我的"]


#不点击的元素
Notclick_name=['电话','联系客服','立即充值','立即开通','立即续费','支付']

#点击的元素
click_name=['永久允许','确定','取消',"关闭"]

#弹窗关闭
tanchuang_close_id=["%s:id/imageview_close"%package,"%s:id/imageview_cloud_sysch_close"%package]


#input中输入,取id
edit_include=["%s:id/edit_search"%package]

#back在就不执行
Notclick_back_include=["%s:id/imageview_back"%package,"返回"]

#edit 输入框，输入值
default_input_values=["你好","hello","霸武凌天"]

#number,name字符串长度
number=20

#截图保存总数
PicNum=100

#存pagesource文件编号
#num=0
#--------------------------------------------------------
#执行顺序
execute_all=["书架","书城","分类","我的"]




#--------------------------------------------------------


if __name__=="__main__":
    print(pageDir)
    print(reportDir)
