一、目前支持的方法
1.caps,设置参数配置，设备名称，包名必须配
2.start，启动设置，start,参数1，配置超时时间
3.left,right,up,down，上下左右滑动
4.id,class,name,text,css,xpath,定位元素，如，id，com.ishugui:id/tv_man，，man;最后一个参数是保存变量名称，定位一组元素
5.click，click,参数1，参数2，参数3，参数1为空，执行上一步的定位元素操作，输入man,之前步中保存的变量名
6.clear，同click
7.input，输入内容，同click
8.sleep--等待时间，秒,
9.savephoto，屏幕截图,图片名称
10.back,手机返回键
11.quit,退出app
12.第1，2行输入2个字符以上或第1行输入#，不执行此行
13.失败重试
14.pagesource
15.assertequals,单个值校验
16.assertequals_all,可以多个值进行校验
17.封装执行函数---
18.assertin,单个值，包含校验
19.toast；
20.定位方法添加elements
21.判断是否存在，存在点击操作，可以用于弹窗的关闭，定位id,name,xpath
22.back多次操作，默认1次
23.坐标点击
24.随机点击 
25.活动当前的activity
26.根据source判断
27.判断不等，不在
28.log，html
29.校验不等于，校验不在里面，
30.

二、环境
1.Java，安卓sdk,appium
2.python 3.x以上
3.python插件安装，运行，setup.py
命令行执行，python setup.py

三、启动设备
1.启动appium
2.连接设备，adb devices，显示设备连接状态

四.运行脚本
1.先将excel数据存放到目录下，目录为datadir
2.再执行runAPPtest.py
命令行执行脚本目录下，执行python runAPPtest.py

五、TODO
1.点击事件
2.坐标点击
3.随机点击
4.长按
5.双指操作，放大，缩小
6.连续点击多次
7.弹窗中的按钮，图片，点击
8.提示信息
9.网络提示信息获取
10.跳转到其他应用判断及返回
11.取当前页面中批量元素，
12.判断元素是否存在与当前页面，然后进行操作
13.报告，统计模块，执行数，失败数，成功数
14.保存定位元素，存为资源，命名：菜单_模块_点位元素
15.if
16.保存元素值，然后进行math，校验
17.H5页面


六、报错
1.元素定位报错
 “...An element could not be located on the page using the given search parameters.”
2.
Message: An unknown server-side error occurred while processing the command.



七、目前支持的定位操作
["id","name","text","css","xpath","class","linktext","partiallinktext","content-desc","textContains","textStartsWith","textMatches","resourceId","resourceIdMatches"]

