一、目前支持的关键字
1.caps,设置参数配置，设备名称，包名必须配
2.start，启动设置，start,参数1，配置超时时间
3.left,right,up,down，上下左右滑动
4.id,class,name,text,css,xpath,定位元素，如，id，com.ishugui:id/tv_man，，man;最后一个参数是保存变量名称
5.click，click,参数1，参数2，参数3，参数1为空，执行上一步的定位元素操作，输入man,之前步中保存的变量名
6.clear，同click
7.input，输入内容，同click
8.sleep--等待时间，秒,
9.savephoto，屏幕截图,图片名称


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
10.assertequals
11.失败重试
12.提取页面，选择true,文字，按钮图标
13.点击手机返回键
14.log
