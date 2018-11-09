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
#设置超时
timeouts=30

#发送post请求的关键字
def post(url,param):
    global session,response,json_res  #引用全局变量
    global paramJson
    #将字符串转换为json
    #param=json_paser(param)
    print('-----------------',type(param))
    param=json.loads(param)
    #param_json() #&格式
    #调用post发送请求
    #res=session.post(url,data=params,verify=False,timeout=timeout)
    print('正在发送post请求-----------------------------')
    print('url--',url)
    print('param--',param)
    print('header--',session.headers)
    res=session.post(url,data=param,verify=False,timeout=timeouts)
    response=res.content.decode('utf8')
    #print("response--",response)
    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,response)

    #print(res,type(res.json()))
    json_res=res.json()
    
    #调用json_paser
    #json_res=json_paser(response)
    print("response--",json_res)


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



#存储url地址
def seturl(url):
    global baseUrl
    baseUrl=url

    
#存储#存储url地址
def settimeout(num):
    global timeouts
    timeouts=num
    print('timeout is setting %s',timeouts)

#add param
def add_param(key,value):
    global paramJson
    paramJson[key]=value
    
    
#json字符串解析,把json字符串解析为字典josn.loads
def json_paser(key):
    global json_res
    #把json字符串解析为字典
    params=json.loads(key)
    print('------------------------',key,params)
    return params


#把值添加到请求头
#3种添加，直接添加，从jkey中取，从保存参数中取
def add_header(hkey,jkey):
    global json_res,session
    temp=jkey
    jsonStr=json_path(jkey)
    #print('----------jsonStr---------------',jsonStr)

    if jsonStr:
        session.headers[hkey]=jsonStr
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,jsonStr)
        print('header[%s]:'%(hkey),session.headers[hkey])

    #取参数值
    elif jkey.startswith('{{'):        
        session.headers[hkey]=get_savejson(jkey)
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,session.headers[hkey])
    #直接添加
    else:
        session.headers[hkey]=jkey
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,session.headers[hkey])
           


#从参数取值：
def get_savejson(key):
    global saveData
    #截取参数key
    key=key[2:len(key)-2]
    return  key
    
    
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
    global  json_res
    
    print('正在校验------------------------------------')
    #用jsonpath取值    
    jsonStr=json_path(key)    
    
    if jsonStr:
        pass

    #期望值从参数取
    if value.startswith('{{'):
        value=get_savejson(value)
        
    print("realresult is %s. the expectedreslut id %s."%(jsonStr,value))
    if jsonStr==value:
        print('校验结果是 PASS')
        #writer.write(reader.rr-1,7,'PASS')
        #writer.write(reader.rr-1,8,value)
    else:
        print('校验结果是 Fail')
        #writer.write(reader.rr-1,7,'Fail')
        #writer.write(reader.rr-1,8,json_res[key])


#jsonpath
def json_path(path):
    global json_res

    #print('------------------------',jsonpath.jsonpath(json_res,path))
    if jsonpath.jsonpath(json_res,path):
        jsonData=jsonpath.jsonpath(json_res,path)
        #print(jsonData)
        #转化为字符串
        jsonStr=str(jsonData[0])
        return  jsonStr
    else:
        pass


#保存值
def saveJson(jkey,key):
    global json_res,saveData
    print("正在保存参数------------------------------------")
    jsonStr=json_path(jkey)    
    saveData[key]=jsonStr
    #writer.write(reader.rr-1,7,'PASS')
    #writer.write(reader.rr-1,8,jsonStr)

    #print('the key is %s \nthe value is : %s'%(key,jsonStr))

    print("保存参数 %s 的值为%s "%(key,jsonStr))



#parse.quote(str1) 编码
def ulrdecode(url):
    urldecode=parse.unquote(url) #解码字符串


def get_code(self):
    #获取返回接口的状态码
    code=response.status_code
    return code

#正则匹配取参数值{{token}}
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
        
    

