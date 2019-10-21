# encoding: utf-8

import os
import time
import sqlite3
import shutil
import json
#import pandas as pd
from tkinter import *
import re
from  tkinter import scrolledtext

apkName = ''
gwei = []
gwei.append('WRITE_CONTACTS')
gwei.append('GET_ACCOUNTS')
gwei.append('READ_CONTACTS')
gwei.append('READ_CALL_LOG')
gwei.append('READ_PHONE_STATE')
gwei.append('CALL_PHONE')
gwei.append('WRITE_CALL_LOG')
gwei.append('USE_SIP')
gwei.append('PROCESS_OUTGOING_CALLS')
gwei.append('ADD_VOICEMAIL')
gwei.append('READ_CALENDAR')
gwei.append('WRITE_CALENDAR')
gwei.append('CAMERA')
gwei.append('BODY_SENSORS')
gwei.append('ACCESS_FINE_LOCATION')
gwei.append('ACCESS_COARSE_LOCATION')
gwei.append('READ_EXTERNAL_STORAGE')
gwei.append('WRITE_EXTERNAL_STORAGE')
gwei.append('RECORD_AUDIO')
gwei.append('READ_SMS')
gwei.append('RECEIVE_WAP_PUSH')
gwei.append('RECEIVE_MMS')
gwei.append('RECEIVE_SMS')
gwei.append('SEND_SMS')
gwei.append('READ_CELL_BROADCASTS')



class Permissions:
    def __init__(self, key, name, isGw):
        self.Key = key
        self.Name = name
        self.Desc = isGw

    pass


def getPermission(key, name):
    isGw = ""
    for item in gwei:
        if item.find(key) >= 0:
            isGw = '敏感'
            pass
        pass

    data = Permissions(key, name, isGw)
    return data


def getAllPermissions():
    allpermissions = []
    allpermissions.append(getPermission('ACCESS_CHECKIN_PROPERTIES', '允许读写访问”properties”表在checkin数据库中，改值可以修改上传'))
    allpermissions.append(getPermission('ACCESS_COARSE_LOCATION', '允许一个程序访问CellID或 WiFi热点来获取粗略的位置'))
    allpermissions.append(getPermission('ACCESS_FINE_LOCATION', '允许一个程序访问CellID或 WiFi热点来获取粗略的位置'))
    allpermissions.append(getPermission('ACCESS_LOCATION_EXTRA_COMMANDS', '允许应用程序访问额外的位置提供命令'))
    allpermissions.append(getPermission('ACCESS_NETWORK_STATE', '允许程序获取网络信息状态，如当前的网络连接是否有效'))
    allpermissions.append(getPermission('ACCESS_NOTIFICATION_POLICY', '希望访问通知策略的应用程序的标记许可'))
    allpermissions.append(getPermission('ACCESS_WIFI_STATE', '允许程序获取当前WiFi接入的状态以及WLAN热点的信息'))
    allpermissions.append(getPermission('ACCOUNT_MANAGER', '允许程序通过账户验证方式访问账户管理ACCOUNT_MANAGER相关信息'))
    allpermissions.append(getPermission('ADD_VOICEMAIL', '允许一个应用程序添加语音邮件系统'))
    allpermissions.append(getPermission('BATTERY_STATS', '允许程序更新手机电池统计信息'))
    allpermissions.append(getPermission('BIND_ACCESSIBILITY_SERVICE', '请求accessibilityservice服务，以确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_APPWIDGET', '允许程序告诉appWidget服务需要访问小插件的数据库，只有非常少的应用才用到此权限'))
    allpermissions.append(getPermission('BIND_CARRIER_MESSAGING_SERVICE', 'API等级高于23时使用,否则使用BIND_CARRIER_SERVICES'))
    allpermissions.append(getPermission('BIND_CARRIER_SERVICES', '允许绑定到运营商应用程序中的服务的系统进程将有这个权限'))
    allpermissions.append(getPermission('BIND_CHOOSER_TARGET_SERVICE', '必须由ChooserTargetService要求，确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_DEVICE_ADMIN', '请求系统管理员接收者receiver，只有系统才能使用'))
    allpermissions.append(getPermission('BIND_DREAM_SERVICE', '必须由一个DreamService要求，确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_INCALL_SERVICE', '必须由一个MidiDeviceService要求，确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_INPUT_METHOD', '请求InputMethodService服务，只有系统才能使用'))
    allpermissions.append(getPermission('BIND_MIDI_DEVICE_SERVICE', '必须由一MidiDeviceService要求，确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_NFC_SERVICE', '由HostApduServiceOffHostApduService必须确保只有系统可以绑定到它'))
    allpermissions.append(
        getPermission('BIND_NOTIFICATION_LISTENER_SERVICE', '必须要求由notificationlistenerservice，以确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_PRINT_SERVICE', '必须要求由printservice，以确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_REMOTEVIEWS', '必须通过RemoteViewsService服务来请求，只有系统才能用'))
    allpermissions.append(getPermission('BIND_TELECOM_CONNECTION_SERVICE', '必须由ConnectionService要求，确保只有系统可以绑定到它'))
    allpermissions.append(
        getPermission('BIND_TEXT_SERVICE', '必须要求textservice(例如吗 spellcheckerservice)，以确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_TV_INPUT', '必须由TvInputService需要确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_VOICE_INTERACTION', '必须VoiceInteractionService要求，确保只有系统可以绑定到它'))
    allpermissions.append(getPermission('BIND_VPN_SERVICE', '绑定VPN服务必须通过VpnService服务来请求,只有系统才能用'))
    allpermissions.append(getPermission('BIND_WALLPAPER', '必须通过WallpaperService服务来请求，只有系统才能用'))
    allpermissions.append(getPermission('BLUETOOTH', '允许程序连接配对过的蓝牙设备'))
    allpermissions.append(getPermission('BLUETOOTH_ADMIN', '允许程序进行发现和配对新的蓝牙设备'))
    allpermissions.append(getPermission('BLUETOOTH_PRIVILEGED', '允许应用程序配对蓝牙设备，而无需用户交互。这不是第三方应用程序可用'))
    allpermissions.append(getPermission('BODY_SENSORS', '允许应用程序访问用户使用的传感器来测量他/她的身体内发生了什么，如心率仪'))
    allpermissions.append(getPermission('BROADCAST_PACKAGE_REMOVED', '允许程序广播一个提示消息在一个应用程序包已经移除后'))
    allpermissions.append(getPermission('BROADCAST_SMS', '允许程序当收到短信时触发一个广播'))
    allpermissions.append(getPermission('BROADCAST_STICKY', '允许程序收到广播后快速收到下一个广播'))
    allpermissions.append(getPermission('BROADCAST_WAP_PUSH', 'WAP PUSH服务收到后触发一个广播'))
    allpermissions.append(getPermission('CALL_PHONE', '允许程序从非系统拨号器里拨打电话'))
    allpermissions.append(getPermission('CALL_PRIVILEGED', '允许程序拨打电话，替换系统的拨号器界面'))
    allpermissions.append(getPermission('CAMERA', '允许程序访问摄像头进行拍照'))
    allpermissions.append(getPermission('CAPTURE_AUDIO_OUTPUT', '允许一个应用程序捕获音频输出。不被第三方应用使用'))
    allpermissions.append(getPermission('CAPTURE_SECURE_VIDEO_OUTPUT', '允许一个应用程序捕获视频输出。不被第三方应用使用'))
    allpermissions.append(getPermission('CAPTURE_VIDEO_OUTPUT', '允许一个应用程序捕获视频输出，不被第三方应用使用'))
    allpermissions.append(getPermission('CHANGE_COMPONENT_ENABLED_STATE', '改变组件是否启用状态'))
    allpermissions.append(getPermission('CHANGE_CONFIGURATION', '允许当前应用改变配置，如定位'))
    allpermissions.append(getPermission('CHANGE_NETWORK_STATE', '允许程序改变网络状态,如是否联网'))
    allpermissions.append(getPermission('CHANGE_WIFI_MULTICAST_STATE', '允许程序改变WiFi多播状态'))
    allpermissions.append(getPermission('CHANGE_WIFI_STATE', '允许程序改变WiFi状态'))
    allpermissions.append(getPermission('CLEAR_APP_CACHE', '允许程序清除应用缓存'))
    allpermissions.append(getPermission('CONTROL_LOCATION_UPDATES', '允许程序获得移动网络定位信息改变'))
    allpermissions.append(getPermission('DELETE_CACHE_FILES', '允许程序删除缓存文件'))
    allpermissions.append(getPermission('DELETE_PACKAGES', '允许程序删除应用'))
    allpermissions.append(getPermission('DIAGNOSTIC', '允许程序到RW到诊断资源'))
    allpermissions.append(getPermission('DISABLE_KEYGUARD', '允许程序禁用键盘锁'))
    allpermissions.append(getPermission('DUMP', '允许程序获取系统dump信息从系统服务'))
    allpermissions.append(getPermission('EXPAND_STATUS_BAR', '允许程序扩展或收缩状态栏'))
    allpermissions.append(getPermission('FACTORY_TEST', '允许程序运行工厂测试模式'))
    allpermissions.append(getPermission('FLASHLIGHT', '允许访问闪光灯'))
    allpermissions.append(getPermission('GET_ACCOUNTS', '允许程序访问账户Gmail列表'))
    allpermissions.append(getPermission('GET_ACCOUNTS_PRIVILEGED', '允许访问帐户服务中的帐户列表'))
    allpermissions.append(getPermission('GET_PACKAGE_SIZE', '允许一个程序获取任何package占用空间容量'))
    allpermissions.append(getPermission('GET_TASKS', '允许一个程序获取信息有关当前或最近运行的任务，一个缩略的任务状态，是否活动等等'))
    allpermissions.append(getPermission('GLOBAL_SEARCH', '允许程序允许全局搜索'))
    allpermissions.append(getPermission('INSTALL_LOCATION_PROVIDER', '允许程序安装定位提供'))
    allpermissions.append(getPermission('INSTALL_PACKAGES', '允许程序安装应用'))
    allpermissions.append(getPermission('INSTALL_SHORTCUT', '创建快捷方式'))
    allpermissions.append(getPermission('INTERNET', '允许程序访问网络连接，可能产生GPRS流量'))
    allpermissions.append(
        getPermission('KILL_BACKGROUND_PROCESSES', '允许程序调用killBackgroundProcesses(String).方法结束后台进程'))
    allpermissions.append(getPermission('LOCATION_HARDWARE', '允许一个应用程序中使用定位功能的硬件，不使用第三方应用'))
    allpermissions.append(getPermission('MANAGE_DOCUMENTS', '允许一个应用程序来管理文档的访问，通常是一个文档选择器部分'))
    allpermissions.append(getPermission('MASTER_CLEAR', '允许程序执行软格式化，删除系统配置信息'))
    allpermissions.append(getPermission('MEDIA_CONTENT_CONTROL', '允许一个应用程序知道什么是播放和控制其内容。不被第三方应用使用'))
    allpermissions.append(getPermission('MODIFY_AUDIO_SETTINGS', '允许程序修改声音设置信息'))
    allpermissions.append(getPermission('MODIFY_PHONE_STATE', '允许程序修改电话状态，如飞行模式，但不包含替换系统拨号器界面'))
    allpermissions.append(getPermission('MOUNT_FORMAT_FILESYSTEMS', '允许程序格式化可移动文件系统，比如格式化清空SD卡'))
    allpermissions.append(getPermission('MOUNT_UNMOUNT_FILESYSTEMS', '允许程序挂载、反挂载外部文件系统'))
    allpermissions.append(getPermission('NFC', '允许程序执行NFC近距离通讯操作，用于移动支持'))
    allpermissions.append(getPermission('PACKAGE_USAGE_STATS', '允许一个程序设置他的activities显示'))
    allpermissions.append(getPermission('PERSISTENT_ACTIVITY', '允许程序创建一个永久的Activity，该功能标记为将来将被移除'))
    allpermissions.append(getPermission('PROCESS_OUTGOING_CALLS', '允许程序监视，修改或放弃播出电话'))
    allpermissions.append(getPermission('READ_CALENDAR', '允许程序读取用户的日程信息'))
    allpermissions.append(getPermission('READ_CALL_LOG', '读取通话记录'))
    allpermissions.append(getPermission('READ_CONTACTS', '允许程序访问联系人通讯录信息'))
    allpermissions.append(getPermission('READ_EXTERNAL_STORAGE',
                                        '程序可以读取设备外部存储空间(内置SDcard和外置SDCard)的文件，如果您的App已经添加了”WRITE_EXTERNAL_STORAGE”权限，则就没必要添加读的权限了，写权限已经包含了读权限了'))
    allpermissions.append(getPermission('READ_FRAME_BUFFER', '允许程序读取帧缓存用于屏幕截图'))
    allpermissions.append(getPermission('READ_INPUT_STATE', '允许程序读取当前键的输入状态，仅用于系统'))
    allpermissions.append(getPermission('READ_LOGS', '允许程序读取系统底层日志'))
    allpermissions.append(getPermission('READ_PHONE_STATE', '允许程序访问电话状态'))
    allpermissions.append(getPermission('READ_SMS', '允许程序读取短信内容'))
    allpermissions.append(getPermission('READ_SYNC_SETTINGS', '允许程序读取同步设置，读取Google在线同步设置'))
    allpermissions.append(getPermission('READ_SYNC_STATS', '允许程序读取同步状态，获得Google在线同步状态'))
    allpermissions.append(getPermission('READ_VOICEMAIL', '允许应用程序在系统读取语音邮件'))
    allpermissions.append(getPermission('REBOOT', '允许程序重新启动设备'))
    allpermissions.append(getPermission('RECEIVE_BOOT_COMPLETED', '允许程序开机自动运行'))
    allpermissions.append(getPermission('RECEIVE_MMS', '允许程序接收彩信'))
    allpermissions.append(getPermission('RECEIVE_SMS', '允许程序接收短信'))
    allpermissions.append(getPermission('RECEIVE_WAP_PUSH', '允许程序接收WAP PUSH信息'))
    allpermissions.append(getPermission('RECORD_AUDIO', '允许程序录制声音通过手机或耳机的麦克'))
    allpermissions.append(getPermission('REORDER_TASKS', '允许程序重新排序系统Z轴运行中的任务'))
    allpermissions.append(getPermission('REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
                                        '权限的应用程序必须要使用ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS这是一个正常的权限：一个应用程序请求它将永远被授予权限，而不需要用户批准或看到它。'))
    allpermissions.append(
        getPermission('REQUEST_INSTALL_PACKAGES', '允许应用程序请求安装包。针对API大于22必须持有该许可使用ACTION_INSTALL_PACKAGE应用。'))
    allpermissions.append(getPermission('RESTART_PACKAGES', '允许程序结束任务通过restartPackage(String)方法，该方式将在外来放弃'))
    allpermissions.append(getPermission('SEND_RESPOND_VIA_MESSAGE', '允许用户在来电的时候用你的应用进行即时的短信息回复'))
    allpermissions.append(getPermission('SEND_SMS', '允许程序发送短信'))
    allpermissions.append(getPermission('SET_ALARM', '允许程序设置闹铃提醒'))
    allpermissions.append(getPermission('SET_ALWAYS_FINISH', '允许程序设置程序在后台是否总是退出'))
    allpermissions.append(getPermission('SET_ANIMATION_SCALE', '允许程序设置全局动画缩放'))
    allpermissions.append(getPermission('SET_DEBUG_APP', '允许程序设置调试程序，一般用于开发'))
    allpermissions.append(
        getPermission('SET_PREFERRED_APPLICATIONS', '允许程序设置应用的参数，已不再工作具体查看addPackageToPreferred(String) 介绍'))
    allpermissions.append(getPermission('SET_PROCESS_LIMIT', '允许程序设置最大的进程数量的限制'))
    allpermissions.append(getPermission('SET_TIME', '允许程序设置系统时间'))
    allpermissions.append(getPermission('SET_TIME_ZONE', '允许程序设置系统时区'))
    allpermissions.append(getPermission('SET_WALLPAPER', '允许程序设置桌面壁纸'))
    allpermissions.append(getPermission('SET_WALLPAPER_HINTS', '允许程序设置壁纸建议'))
    allpermissions.append(getPermission('SIGNAL_PERSISTENT_PROCESSES', '允许程序发送一个永久的进程信号'))
    allpermissions.append(getPermission('STATUS_BAR', '允许程序打开、关闭、禁用状态栏'))
    allpermissions.append(getPermission('SYSTEM_ALERT_WINDOW', '允许程序显示系统窗口'))
    allpermissions.append(getPermission('TRANSMIT_IR', '允许使用设备的红外发射器，如果可用'))
    allpermissions.append(getPermission('UNINSTALL_SHORTCUT', '删除快捷方式'))
    allpermissions.append(getPermission('UPDATE_DEVICE_STATS', '允许程序更新设备状态'))
    allpermissions.append(getPermission('USE_FINGERPRINT', '允许应用程序使用指纹硬件'))
    allpermissions.append(getPermission('USE_SIP', '允许程序使用SIP视频服务'))
    allpermissions.append(getPermission('VIBRATE', '允许程序振动'))
    allpermissions.append(getPermission('WAKE_LOCK', '允许程序在手机屏幕关闭后后台进程仍然运行'))
    allpermissions.append(getPermission('WRITE_APN_SETTINGS', '允许程序写入网络GPRS接入点设置'))
    allpermissions.append(getPermission('WRITE_CALENDAR', '允许程序写入日程，但不可读取'))
    allpermissions.append(getPermission('WRITE_CALL_LOG', '允许程序写入（但是不能读）用户的联系人数据'))
    allpermissions.append(getPermission('WRITE_CONTACTS', '写入联系人,但不可读取'))
    allpermissions.append(getPermission('WRITE_EXTERNAL_STORAGE', '允许程序写入外部存储,如SD卡上写文件'))
    allpermissions.append(getPermission('WRITE_GSERVICES', '允许程序修改Google服务地图'))
    allpermissions.append(getPermission('WRITE_SECURE_SETTINGS', '允许应用程序读取或写入安全系统设置'))
    allpermissions.append(getPermission('WRITE_SETTINGS', '允许程序读取或写入系统设置'))
    allpermissions.append(getPermission('WRITE_SYNC_SETTINGS', '允许程序写入同步设置'))
    allpermissions.append(getPermission('WRITE_VOICEMAIL', '允许应用程序修改和删除系统中的现有的语音邮件，只有系统才能使用'))
    allpermissions.append(getPermission('INTERACT_ACROSS_USERS',
                                        'getCurrentUser() 是AMS中的一个接口，用来获取当前用户,这里会检查 是否有 INTERACT_ACROSS_USERS 和 INTERACT_ACROSS_USERS_FULL 这两个权限'))
    allpermissions.append(getPermission('UPDATE_APP_OPS_STATS',
                                        'API 18 添加AppOpsManager(被隐藏，在Android 4.4公开）API 21 后需要签名验证的权限android.Manifest.permission.UPDATE_APP_OPS_STATS，第三方应用用不了了'))
    allpermissions.append(getPermission('BROADCAST_PACKAGE_ADDED', '监听app安装'))
    allpermissions.append(getPermission('INSTALL', '监听app安装'))
    allpermissions.append(getPermission('REPLACED', '监听app更新被替换'))
    allpermissions.append(getPermission('BROADCAST_PACKAGE_CHANGED', '应用被改变，譬如某些组件被disable/enable'))
    allpermissions.append(getPermission('ACCESS_DOWNLOAD_MANAGER', '申请访问DownloadManager的权限'))
    allpermissions.append(getPermission('getui.permission.GetuiService', '个推自定义权限'))
    return allpermissions


def getPermissionName(key):
    name = '未知'
    desc = ''

    for item in getAllPermissions():
        if key.find(item.Key) >= 0:
            # print(item.Key + '====' + item.Name + "====" + item.Desc)
            name = item.Name
            desc = item.Desc
            return name, desc
    return name, desc
    pass


def getApkInfo(key):
    with open('./dump1.txt', 'w', encoding='utf-8') as f1:
        f1.write('')
    time.sleep(1)
    os.popen('aapt dump badging' +' ' + apkName + 'dump1.txt')
    time.sleep(1)
    with open('./dump1.txt','r',encoding='utf-8') as f1:
        res = f1.read()
    return str(res.split(key + '=')[1]).split(' ')[0]
    pass

    # pack(data)


def getApkPermissions():
    with open('./dump2.txt', 'w') as f2:
        f2.write('')
    permissions = []
    os.popen('aapt dump badging' +' '+ apkName + '> dump2.txt')
    time.sleep(1)
    with open('./dump2.txt','r',encoding='utf-8') as f2:
        res = f2.read()
    aa = res.split('\n')
    for item in aa:
        # print(item)
        if item.find('uses-permission') >= 0:
            name, desc = getPermissionName(item)
            obj = {'permission': item, 'name': name, 'desc': desc}
            permissions.append(obj)
            # print(item)
    return permissions
    pass

def getname(file):
    zz = '(\w+\.apk)'
    name = re.findall(zz,file,flags=0)[0]
    return name

getname("""D:\我的文档/app自动化\checkApk\checkApk\pack/test.apk""")


# print('versionName:', getApkInfo('versionName'))
# print('label:', getApkInfo('label'))
# print('versionCode:', getApkInfo('versionCode'))
# print('package_name:', getApkInfo('package: name'))
# ''''
# aapt d permissions <apk文件>'''


def getquanxian():
    global apkName
    ST.delete(1.0,END)
    apkName = E1.get()
    name = apkName
    if apkName == '':
        ST.insert(END,'请填写apk路径')
        return
    elif "\\" in apkName or "/" in apkName:
        name = getname(apkName)
    else:
        apkName = "./apk/"+apkName
    conn = sqlite3.connect(':memory:')
    sql = '''create table quanxian (
            `权限` text,
            `权限描述` text,
            `危险等级` intextteger
            )'''
    cursor = conn.cursor()
    cursor.execute(sql)
    permissions = getApkPermissions()
    data = []
    for permission in permissions:
        try:
            print(permission)
            # ST.insert(END, permission)
            data.append((str(permission['permission']), str(permission['name']), str(permission['desc'])))
        except Exception as e:
            print('异常:', e)
            ST.insert(END, '异常:'+e)
            pass
        pass

    try:
        save_sql = 'INSERT INTO quanxian values (?, ?, ?)'
        print('sql_one:', save_sql)
        # ST.insert(END, 'sql_one:' + save_sql)
        cursor.executemany(save_sql, data)
    except Exception as e:
        print('异常:', e)
        ST.insert(END, '异常:' + e)
        pass

    cursor.close()
    table = pd.read_sql("select * from quanxian", conn)
    table2 = pd.read_sql("select * from quanxian where 危险等级 = '敏感'", conn)
    print('table:', table)
    pd.DataFrame(table).to_excel(os.getcwd() + "/report/%s权限" %name + ".xlsx", sheet_name="权限", index=False, header=True)
    print('完成')

    print("table2:"+table2)
    ST.insert(END,table2)
    ST.insert(END,"详细报告已生成至report目录")
    pass


# getquanxian()
# print('permissions:', getApkPermissions())

'''
self.Key = key
        self.Name = name
        self.Desc = isGw
'''





top = Tk()
top.geometry('600x400')
top.wm_title('APK敏感权限扫描工具-V1.1.0')

L2NR = StringVar()
L2NR.set('')

L1 = Label(top,text = '请填入待测apk路径：',width = 20,height = 2)
L1.grid(row =0,column = 0)
E1 = Entry(top, width = 40)
E1.grid(row = 0,column = 1)
B1= Button(top,text = '执行',command = getquanxian,width = 40,height = 3)
B1.grid(row = 1,column = 0,columnspan =2)
# L2 = Label(top,textvariable = L2NR,anchor = NW,width = 60,height = 20)
# L2.grid(row =2 ,column = 0,columnspan =2)
ST= scrolledtext.ScrolledText(top,width = 80,height = 20)
ST.grid(row = 2,column = 0,columnspan =3)

top.mainloop()