# coding:utf-8
from common import Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
import re


'''
s='{"pub":{"deviceId":"dzf17037bc2847490eac50634882321b77","subPline":"2","screen":"1080x1920","appCode":"ishugui","userId":"214569066","dzPaySupport":"2","city":"北京","apiVersion":"3.8.4.2051","province":"北京市","v":"4","imei":"867392038724947","p":"33","clientAgent":"svnVer_1811061002","lsw":"1","apn":"wifi","imsi":"460025012052565","channelFee":"K101064","cmTel":"","pname":"com.ishugui","channelCode":"Google","cme":"0","os":"android25","brand":"Xiaomi","macAddr":"04:B1:67:52:A7:7E","model":"Mi Note 3"},"pri":{}} {""pri"": {}, ""pub"": {""city"": ""北京"", ""lsw"": ""1"", ""screen"": ""1080x1920"", ""userId"": ""214569066"", ""province"": ""北京市"", ""p"": ""33"", ""imsi"": ""460025012052565"", ""macAddr"": ""04:B1:67:52:A7:7E"", ""clientAgent"": ""svnVer_1811061002"", ""os"": ""android25"", ""channelCode"": ""Google"", ""deviceId"": ""dzf17037bc2847490eac50634882321b77"", ""pname"": ""com.ishugui"", ""imei"": ""867392038724947"", ""dzPaySupport"": ""2"", ""cme"": ""0"", ""apn"": ""wifi"", ""appCode"": ""ishugui"", ""subPline"": ""2"", ""cmTel"": """", ""apiVersion"": ""3.8.4.2051"", ""brand"": ""Xiaomi"", ""model"": ""Mi Note 3"", ""channelFee"": ""K101064"", ""v"": ""4""}}'

def re_compile(srcStr):
    findword="({{[a-zA-Z]+}})"  
    pattern = re.compile(findword)
    results =pattern.findall(srcStr)    

    for result in results: 
        print (result)     
    
    #找到匹配的参数,替换参数值,未找到就原来的
    if len(results)!=0:
        for result in results: 
            print ('--正在替换---------------------',result)
    else:
        print(1)

re_compile(s)
'''


'''
url="http://api.ishugui.com/asg/portal/call/242.do"
paramstr='{"pub":{"deviceId":"dzf17037bc2847490eac50634882321b77","subPline":"2","screen":"1080x1920","appCode":"ishugui","userId":"214569066","dzPaySupport":"2","city":"北京","apiVersion":"3.8.4.2051","province":"北京市","v":"4","imei":"867392038724947","p":"33","clientAgent":"svnVer_1811061002","lsw":"1","apn":"wifi","imsi":"460025012052565","channelFee":"K101064","cmTel":"","pname":"com.ishugui","channelCode":"Google","cme":"0","os":"android25","brand":"Xiaomi","macAddr":"04:B1:67:52:A7:7E","model":"Mi Note 3"},"pri":{}}'



header={}
header["Content-Type"]="application/json;charset=utf-8"

Http.add_header("Content-Type","application/json;charset=utf-8")

Http.post(url,paramstr)

Http.saveJson("$['pub']['status']","userid")
Http.assert_equals("$['pub']['status']","{{userid}}")
'''
'''
{'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.18.4', 'Content-Type': 'application/json', 'Accept': '*/*'}

url="http://ceshi.farmfriend.com.cn/management/sys/login"
paramstr="userName=123&password=123456"


Http.add_header("Content-Type","application/json;charset=utf-8")

Http.post(url,paramstr)


#Http.saveJson("$['pub']['status']","userid")
#Http.assert_equals("$['pub']['status']","{{userid}}")


url="http://config.pinyin.sogou.com/api/toolbox/geturl.php?h=4F6E575CBA26F6F63F952FF96E599433&v=9.1.0.2589&r=6990_sogou_pinyin_8.6.0.1423_6990"
paramstr=""
Http.api_request('get',url,"")

'''

srcfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\autoTestApi\datadir\myapp_Http.xls"
desfile=r"E:\myworkspace\mygit\mygitworkspace\autoAPI\autoTestApi\datadir\myapp_Http333_result.xls"

def run(line):
    if line[3]=='post':
        Http.api_request('post',line[4],line[5])
        return
    if line[3]=='get':
        Http.api_request('get',line[4],line[5])
        return
    if line[3]=='put':
        Http.api_request('put',line[4],line[5])
        return

    if line[3]=='addheader':
        Http.add_header(line[4],line[5])
        return
    if line[3]=='assertequals':
        Http.assert_equals(line[4],line[5])
        return
    if line[3]=='savejson':
        Http.saveJson(line[4],line[5])
        return
    if  line[3]=='seturl':
        Http.seturl(line[4])
        return
    if  line[3]=='settimeout':
        Http.settimeout(line[4])
        return
    if  line[3]=='addparam':
        Http.add_param(line[4],line[5])
        return
    if  line[3]=='removeheader':
        Http.remove_header(line[4])
        return
        

def all():
    reader.open_excel(srcfile)
    writer.copy_open(srcfile,desfile)
    num=0
    for i in range(0,reader.r):
        line=reader.readline()
        print(line)
        if len(line[0])>2 or len(line[1])>2:
            #不去执行的行
            pass
        else:
            #执行
            num=num+1
            print('正在执行 第%s个.....'%(num))
            run(line)
            
            
            pass
                                                            
    writer.save_close()

all()
