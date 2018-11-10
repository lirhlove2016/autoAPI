# coding:utf-8
import requests
import json
from common import readexcel as reader,writeexcel as writer
from urllib import parse
import jsonpath
import re

session=requests.Session()
#保存请求结果
response=''
#保存解析后的json字典
json_res=''

#存储值字典
saveData={}
baseUrl=''
#添加入参
paramJson={}
#设置超时
timeouts=30

#根据不同方法访问接口
def api_method(method,url,param):
	#print('start request-----------------------------------------------')
	if method=='post':
            r=session.post(url,data=param,verify=False,timeout=timeouts)
            return r

	elif method=='get':
	    r=session.get(url,params=param,verify=False,timeout=timeouts)
	    return r
	elif method=='put':
	    r=session.put(url,params=param,verify=False,timeout=timeouts)
	    return r

	else:
	    print('%s is error.'%method)
	

#发送post请求的关键字
def api_request(method,url,param):
    global session,response,json_res  #引用全局变量
    global paramJson   #读取存储的入参

    #参数不为空
    #json格式的转换
    if param.startswith('{'):
        print('----------------------',type(param))
        if param:
            #从参数取{{}}
            param=re_compile(param)
            params=json_paser(param)
            
        else:
            params=param
   
    #参数是&格式，将字符串转换为json
    else:
        params=param_json(param)

    print('正在发送post请求-----------------------------')
    print('url--',url)
    print('param--',param)
    print('header--',session.headers)
    #调用
    res=api_method(method,url,params)
    response=res.content.decode('utf8')
    #print("response--",response)
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,response)

    #print(res,type(res.json()))
    #json_res=res.json()

    if response.startswith('{'):
        #调用json_paser
        json_res=json_paser(response)
    else:
         json_res=response
    print("response--",json_res)


#存储url地址
def seturl(url):
    global baseUrl
    baseUrl=url
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,baseUrl)
    
#存储#存储url地址
def settimeout(num):
    global timeouts
    timeouts=int(num)
    print('timeout is setting %s',timeouts)
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,timeouts)  

#add param
def add_param(key,value):
    global paramJson
    paramJson[key]=value
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,value)      

    
#json字符串解析,把json字符串解析为字典josn.loads
def json_paser(value):
    global json_res
    #把json字符串解析为字典
    params=json.loads(value)
    return params


#把值添加到请求头
#3种添加，直接添加，从jkey中取，从保存参数中取
def add_header(hkey,jkey):
    global json_res,session
    
    if len(jkey)!=0:
        #取值，未取到就原来的值
        jsonStr=json_path(jkey)
        if jsonStr:
            session.headers[hkey]=jsonStr
            writer.write(reader.rr-1,7,'PASS')
            writer.write(reader.rr-1,8,jsonStr)
            print('header[%s]:'%(hkey),session.headers[hkey])

        #取参数值
        elif jkey.startswith('{{'):        
            session.headers[hkey]=get_savejson(jkey)
            writer.write(reader.rr-1,7,'PASS')
            writer.write(reader.rr-1,8,session.headers[hkey])
    #jkey为空
    else:
        session.headers[hkey]=jkey
        writer.write(reader.rr-1,7,'PASS')
        writer.write(reader.rr-1,8,session.headers[hkey])
           
  
#删除请求头信息
def remove_header(key):
    global json_res,session
    del session.headers[key]

    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,json_res[jkey])
    print('remove  header[%s] success.'%(key),session.headers)

    
#参数&格式转换为字典
def param_json(param):
    params={}
    #如果参数不为空就处理为字典
    #从参数取{{}}
    param=re_compile(param)
    
    if len(param)>1:
        p=param.split('&')
        print(p)
        for pp in p:
            ppp=pp.split('=')
            params[ppp[0]]=ppp[1]
        print(params)
    
    return params

#断言
def assert_equals(key,value):
    global  json_res    
    print('正在校验------------------------------------')
    #用jsonpath取值    
    jsonStr=json_path(key)
    
     
    #如果有取值就用保存的参数
    value=re_compile(value)        
    print("realresult is %s. the expectedreslut id %s."%(jsonStr,value))

    if jsonStr==value:
        print('校验结果是 PASS')
        writer.write(reader.rr-1,7,'PASS')
        writer.write(reader.rr-1,8,value)
    else:
        print('校验结果是 Fail')
        writer.write(reader.rr-1,7,'Fail')
        writer.write(reader.rr-1,8,value)


#jsonpath
def json_path(path):
    global json_res

    print('--------JSONPATH----------------',jsonpath.jsonpath(json_res,path))
    if jsonpath.jsonpath(json_res,path):
        jsonData=jsonpath.jsonpath(json_res,path)
        #print(jsonData)
        #转化为字符串
        jsonStr=str(jsonData[0])
        return  jsonStr
    else:
        return  path


#从参数取值：
def get_savejson(key):
    global saveData

    #取参数key
    key=key[2:len(key)-2]    
    print('the key is %s and value is %s '%(key,saveData[key]))
    return  saveData[key]
    


#保存值
def saveJson(jkey,key):
    global json_res,saveData
    print("正在保存参数------------------------------------")
    jsonStr=json_path(jkey)    
    saveData[key]=jsonStr
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,jsonStr)

    #print('the key is %s \nthe value is : %s'%(key,jsonStr))

    print("保存参数 %s 的值为%s "%(key,jsonStr))



#parse.quote(str1) 编码
def ulr_decode(url):
    urldecode=parse.unquote(url) #解码字符串
    writer.write(reader.rr-1,7,'PASS')
    writer.write(reader.rr-1,8,urldecode)

def get_code(self):
    #获取返回接口的状态码
    code=response.status_code
    return code


#正则匹配取参数值{{token}}
def re_compile(srcStr):
    #print('正则匹配-----------------',type(srcStr))
    findword="({{[a-zA-Z]+}})"  
    pattern = re.compile(findword)
    results =pattern.findall(srcStr)    

    #for result in results: 
        #print (result)     
    
    #找到匹配的参数,替换参数值,未找到就原来的
    if len(results)!=0:
        for result in results: 
            #print ('--正在替换---------------------',result)
            temp=get_savejson(result)           
            srcStr=srcStr.replace(result,temp)

        return   srcStr
    else:
        return srcStr

    

