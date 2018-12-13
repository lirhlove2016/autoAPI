一、目前支持的关键字
1.caps,设置参数配置，设备名称，包名必须配
2.start，启动设置
3.swip，左右上下
4.id,class,name,text,css,xpath
5.click
6.clear
7.input，输入内容
8.sleep--等待时间，秒
9.savephoto，屏幕截图
10.assertequals---未实现
11.失败重试------未实现
12.提取页面，选择true,文字，按钮图标，-未实现
13.点击手机返回键-未实现
14.log---未实现

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

五、安卓6.0，8.0区别