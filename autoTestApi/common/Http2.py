# coding:utf-8
import requests
import json
from common import readexcel as reader,writeexcel as writer
from urllib import parse
import jsonpath

session=requests.Session()
#保存请求结果
response=''
#保存解析后的json字典
json_res=''

params={}

#存储值字典
saveData={}
baseUrl=''
paramJson={}

#发送post请求的关键字
def post(url,param):
    global session,response,json_res  #引用全局变量
    global paramJson
    #将字符串转换为json
    param=json_paser(param)
    print('---------------------',type(param),param)
    #param_json() #&格式
    #调用post发送请求
    #res=session.post(url,data=params,verify=False,timeout=30)
    res=session.post(url,data=param,verify=False,timeout=30)
    response=res.content.decode('utf8')
    print(response)
    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,response)

    #print(res,type(res.json()))
    json_res=res.json()
    
    #调用json_paser
    #json_res=json_paser(response)
    print(json_res)

#发送get请求的关键字
def get(url,param):
    global session,response  #引用全局变量
    #param_json() 
    #调get发送请求
    res=session.get(url,data=param,verify=False,timeout=30)
    response=res.content.decode('utf8')
    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,response) 
   
    print(response)
    #调用json_paser
    json_paser(response)

#add param
def add_param(key,value):
    global paramJson
    paramJson[key]=value
    
    
#json字符串解析,把json字符串解析为字典josn.loads
def json_paser(key):
    global json_res
    #把json字符串解析为字典
    return json.loads(key)


#把值添加到请求头
def add_header(hkey,jkey):
    global json_res,session
    temp=jkey
    jsonStr=json_path(jkey)
    print('----------jsonStr---------------',jsonStr)
    if jsonStr:
        session.headers[hkey]=jsonStr
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,json_res[jkey])
        print('header[%s]:'%(hkey),session.headers[hkey])

    elif jkey.startswith('{{'):        
        session.headers[hkey]=get_savejson(jkey)

    else:
        session.headers[hkey]=jkey
           


#从参数取值：
def get_savejson(key):
    global saveData
    #截取参数key
    key=key[2:len(key)-2]
    return saveData[key]
    

    
#删除请求头信息
def remove_header(key):
    global json_res,session
    print('------------------------------',session.headers)
    del session.headers[key]

    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,json_res[jkey])
    print('remove  header[%s] success.'%(key),session.headers)

    
#参数&格式转换为字典
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

#断言
def assert_equals(key,value):
    global json_res
    print(value)
    #用jsonpath取值    
    #jsonData=jsonpath.jsonpath(json_res,key)
    jsonStr=json_path(key)    
    print(" the value is %s  "%(jsonStr))
    print('----------jsonStr---------------',jsonStr,type(jsonStr))
    if jsonStr:
        pass

    #期望值从参数取
    if value.startswith('{{'):
        value=get_savejson(value)
        print(type(jsonStr))
    
    if jsonStr==value:
        print('PASS')
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,value)
    else:
        print('Fail')
        #writer.write(reader.rr-1,7,'Fail')
        #writer.write(reader.rr-1,8,json_res[key])

#jsonpath
def json_path(path):
    global json_res
    #print('json_res :',json_res)
    print('------------------------',jsonpath.jsonpath(json_res,path))
    if jsonpath.jsonpath(json_res,path):
        jsonData=jsonpath.jsonpath(json_res,path)
        print(jsonData)
        #转化为字符串
        jsonStr=str(jsonData[0])
        return  jsonStr
    else:
        pass


#保存值
def saveJson(jkey,key):
    global json_res,saveData
    jsonStr=json_path(jkey)    
    saveData[key]=jsonStr
    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,jsonStr)
    print('the key is %s \nthe value is : %s'%(key,jsonStr))
    
    print("------------------saveData------------",saveData)


#存储url地址
def seturl(url):
    global baseUrl
    baseUrl=url



#parse.quote(str1) 编码
def ulrdecode(url):
    urldecode=parse.unquote(url) #解码字符串


def get_code(self):
    #获取返回接口的状态码
    code=response.status_code
    return code


def re_compile(src):
    findword="({{[a-zA-Z]+}})"  
    pattern = re.compile(findword)
    results =  pattern.findall(temp)    
    for result in results: 
        print (result)  
    
    return results
    #替代 {{id}}
    if len(results)!=0:
        pass
        
    

