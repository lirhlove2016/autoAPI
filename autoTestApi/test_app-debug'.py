# coding:utf-8
from common import Http2 as Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
#jsonpath.jsonpath(json,"$['store']['book'][0]['author']")

url="http://api.ishugui.com/asg/portal/call/242.do"
paramstr='{"pub":{"deviceId":"dzf17037bc2847490eac50634882321b77","subPline":"2","screen":"1080x1920","appCode":"ishugui","userId":"214569066","dzPaySupport":"2","city":"北京","apiVersion":"3.8.4.2051","province":"北京市","v":"4","imei":"867392038724947","p":"33","clientAgent":"svnVer_1811061002","lsw":"1","apn":"wifi","imsi":"460025012052565","channelFee":"K101064","cmTel":"","pname":"com.ishugui","channelCode":"Google","cme":"0","os":"android25","brand":"Xiaomi","macAddr":"04:B1:67:52:A7:7E","model":"Mi Note 3"},"pri":{}}'

header={}
header["Content-Type"]="application/json;charset=utf-8"

Http.add_header("Content-Type","application/json;charset=utf-8")

Http.post(url,paramstr)

Http.saveJson("$['pub']['status']","userid")
Http.assert_equals("$['pub']['status']","{{userid}}")

srcfile="E:\\myworkspace\\mygit\\mygitworkspace\\autoAPI\\autoTestApi\\datadir\\myapp_Http.xls"
desfile="E:\\myworkspace\\mygit\\mygitworkspace\\autoAPI\\autoTestApi\\datadir\\myHttp_result.xls"


def run(line):
    if line[3]=='post':
        Http.post(line[4],line[5])
        return
    if line[3]=='get':
        Http.get(line[4],line[5])
        return
    if line[3]=='addheader':
        Http.add_header(line[4],line[5])
        return
    if line[3]=='assertequals':
        Http.assert_equals(line[4],line[5])
        return
    if line[3]=='savajson':
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
        

reader.open_excel(srcfile)
writer.copy_open(srcfile,desfile)

for i in range(0,reader.r):
    line=reader.readline()
    print(line)
    if len(line[0])>2 or len(line[1])>2:
        #不去执行的行
        pass
    else:
        #执行
        run(line)
        pass
                                                        
writer.save_close()


