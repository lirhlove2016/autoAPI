# coding:utf-8
from common import Http2 as Http
from common import readexcel as reader,writeexcel as writer
import json
import jsonpath
#jsonpath.jsonpath(json,"$['store']['book'][0]['author']")

url="http://api.ishugui.com/asg/portal/call/242.do"
paramstr='{"pub":{"deviceId":"dzf17037bc2847490eac50634882321b77","subPline":"2","screen":"1080x1920","appCode":"ishugui","userId":"214569066","dzPaySupport":"2","city":"北京","apiVersion":"3.8.4.2051","province":"北京市","v":"4","imei":"867392038724947","p":"33","clientAgent":"svnVer_1811061002","lsw":"1","apn":"wifi","imsi":"460025012052565","channelFee":"K101064","cmTel":"","pname":"com.ishugui","channelCode":"Google","cme":"0","os":"android25","brand":"Xiaomi","macAddr":"04:B1:67:52:A7:7E","model":"Mi Note 3"},"pri":{}}'

print('-------------------------',type(paramstr))
header={}
header["Content-Type"]="application/json;charset=utf-8"
print('url-----------',url)
print('param---------',paramstr)
print('header---------',header)

print(type(paramstr))
#转化为json
#paramjson=json.loads(paramstr)
#print('paramjson--------------',paramjson)
#print(type(paramjson))

Http.post(url,paramstr)


"""
'''
json_res={"pub":{"status":4}}

s=jsonpath.jsonpath(json_res, "$['pub']['status']")
print(s,type(s))

"""
"""
Http.assert_equals("$['pub']['status']",'4')

Http.add_header("Content-Type",'pub')
Http.saveJson('userid',"$['pub']['status']")

Http.assert_equals("$['pub']['status']",'4')

Http.add_header("Content-Type",'pub')

print('------------------------------------------------------')

Http.add_header("content-Type",'pub')
Http.add_header("content-Type",'pub')
Http.add_header("content-Type",'pub')
Http.add_header("mykey1","$['pub']['status']")
Http.add_header("mykey2","$['pub']")
Http.add_header("mykey3","pub")

Http.add_header("mykey3","applicationdaf asd")
Http.add_header("mykey3","applicationdaf asd")
key="{{id}"

Http.remove_header("content-Type")
"""
print('------------------------------------------------------')

Http.saveJson("$['pub']['status']","userid")
Http.assert_equals("$['pub']['status']","{{userid}}")

