# coding:utf-8
import requests
import json
from common import readexcel as reader,writeexcel as writer
from urllib import parse

session=requests.Session()
#保存请求结果
response=''
#保存解析后的json字典
json_res=''

params={}
param=''
#存储值字典
saveparam={}
base_url=''

#发送post请求的关键字
def post(url,param):
    global session,response  #引用全局变量
    #param_json() 
    #调用post发送请求
    #res=session.post(url,data=params,verify=False,timeout=30)
    res=session.post(url,data=param,verify=False,timeout=30)
    response=res.content.decode('utf8')

    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,response)

    #print(res,type(res.json()))
    print(response)
    #调用json_paser
    json_paser()

#发送get请求的关键字
def get(url,param):
    global session,response  #引用全局变量
    #param_json() 
    #调get发送请求
    #res=session.post(url,data=params,verify=False,timeout=30)
    res=session.get(url,data=param,verify=False,timeout=30)
    response=res.content.decode('utf8')
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,response) 
   
    print(response)
    #调用json_paser
    json_paser()

#json字符串解析,把json字符串解析为字典josn.loads
def json_paser():
    global json_res
    #把json字符串解析为字典
    json_res=json.loads(response)
    #获取值
    print(json_res['errmsg'])

#把值添加到请求头
def add_header(hkey,jkey):
    global json_res,session

    session.headers[hkey]=json_res[jkey]
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,json_res[jkey])
    print('headers[%s]:'%(session.headers[hkey]),session.headers[hkey])


#参数转换为字典
def param_json():
    global params
    #如果参数不为空就处理为字典
    params={}

    if len(param)>1:
        p=param.split('&')
        print(p)
        for pp in p:
            ppp=pp.split('=')
            params[ppp[0]]=ppp[1]
        print(params)

#保存值
def saveJson(jkey,key):
    global json_res,saveparam
    saveparam[key]=json_res[jkey]
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,json_res[jkey])
    print('保存%s 的值是: %s'%(key,json_res[jkey]))


#断言
def assert_equals(key,value):
    global json_res
    print(value)
    #转化为字符串
    if json_res[key].__str__()==value:
        print('PASS')
        writer.write(reader.rr-1,7,'PASS')
        writer.write(reader.rr-1,8,value)
    else:
        print('Fail')
        writer.write(reader.rr-1,7,'Fail')
        writer.write(reader.rr-1,8,json_res[key])

def seturl(url):
    global base_url
    base_url=url
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,base_url)

#parse.quote(str1) 编码
def ulrdecode(url):
    urldecode=parse.unquote(url) #解码字符串


def get_code(self):
    #获取返回接口的状态码
    code=self.api_request().status_code
    return code

def get_json(self):
    #获取返回信息json数据
    json_data=self.api_request().json()
    return json_data



