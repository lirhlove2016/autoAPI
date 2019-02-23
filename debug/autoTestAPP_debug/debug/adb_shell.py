import subprocess

#ADB执行命令行,包括一些常用命令
class ADBShell:
    def __init__(self, adb_path=""):
        self.adb_path = adb_path

    def invoke(self,cmd):
        output, errors = subprocess.Popen(self.adb_path+" "+cmd, shell=True,
                stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o

    def getDevices(self):
        android_devices_list = []
        for device in self.invoke('devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list
class Device:
    def __init__(self,adb_shell,device_id):
        self.device_id = device_id
        self.adb_shell = adb_shell

    def get_device_info(self):
        device_adb = DeviceADB(self.adb_shell,self.device_id)
        return DeviceInfo(self.device_id, "Android", device_adb.get_android_version(),
                device_adb.get_sdk_version(),device_adb.get_product_brand(),
                device_adb.get_product_model(),device_adb.get_product_rom())


class DeviceInfo:
    def __init__(self, uid, os_type, os_version, sdk_version, brand, model, rom_version):
        self.uid = uid
        self.os_type = os_type
        self.os_version = os_version
        self.sdk_version = sdk_version
        self.brand = brand
        self.model = model
        self.rom_version = rom_version
    def __repr__(self):
        str = "设备ID:"+self.uid+"\n"
        str = str+"操作系统："+self.os_type+"\n"
        str = str+"操作系统版本："+self.os_version+"\n"
        str = str + "SDK版本：" + self.sdk_version + "\n"
        str = str + "设备品牌：" + self.brand + "\n"
        str = str + "设备型号：" + self.model + "\n"
        str = str + "ROM版本：" + self.rom_version
        return str


'''
ADB options on a devices
init_param:the device id    
'''
class DeviceADB(object):
    def __init__(self,adbShell, device_id):
    #device_id为需要操作的设备ID
        self.adbShell = adbShell
        self.device_id = "-s %s" % device_id
    def adb(self, args):
    #在设备上执行adb命令
        cmd = "%s %s" % (self.device_id, str(args))
        return self.adbShell.invoke(cmd)
    def shell(self, args):
        cmd = "%s shell %s" % (self.device_id, str(args),)
        return self.adbShell.invoke(cmd)

    def get_device_state(self):
    #获取设备状态： offline | bootloader | device
        return self.adb("get-state").stdout.read().strip()
    def get_device_id(self):
    #获取设备id号，return serialNo
        return self.adb("get-serialno").stdout.read().strip()
    def get_android_version(self):
    #获取设备中的Android版本号，如4.2.2
        return self.shell("getprop ro.build.version.release").strip()
    def get_sdk_version(self):
    #获取设备SDK版本号，如：24
        return self.shell("getprop ro.build.version.sdk").strip()
    def get_product_brand(self):
    #获取设备品牌，如：HUAWEI
        return self.shell("getprop ro.product.brand").strip()
    def get_product_model(self):
    #获取设备型号，如：MHA-AL00
        return self.shell("getprop ro.product.model").strip()
    def get_product_rom(self):
    #获取设备ROM名，如：MHA-AL00C00B213
        return self.shell("getprop ro.build.display.id").strip()

if __name__=='__main__':

