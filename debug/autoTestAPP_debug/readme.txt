一、目前支持的方法
1.caps,设置参数配置，设备名称，包名必须配
2.start，启动设置，start,参数1，配置超时时间
3.left,right,up,down，上下左右滑动
4.id,class,name,text,css,xpath,定位元素，如，id，com.ishugui:id/tv_man，，man;最后一个参数是保存变量名称
5.click，click,参数1，参数2，参数3，参数1为空，执行上一步的定位元素操作，输入man,之前步中保存的变量名
6.clear，同click
7.input，输入内容，同click
8.sleep--等待时间，秒,
9.savephoto，屏幕截图,图片名称
10.back,手机返回键
11.quit,退出app
12.第1，2行输入2个字符以上或第1行输入#，不执行此行
13.失败重试

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
1.assertequals
2.提取页面，选择true,文字，按钮图标
3.log

六、报错
1.元素定位报错
 “...An element could not be located on the page using the given search parameters.”
2.有正在运行的
Message: An unknown server-side error occurred while processing the command.

注意：安卓6.0，8.0区别

七、打包exe文件需要
打包命令,cmd进入目录下，输入：pyinstall -F  runAPPtest.py
修改run 和 element文件下conf_exe目录