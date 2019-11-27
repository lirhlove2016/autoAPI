import requests
import json

#post请求

baseurl="http://192.168.0.20:3080/asg/portal/call/"

json_data={"pub":{"deviceId":"dz6wb100971030761d39e7145a3850eedc4563e61ff","subPline":"2","screen":"1080x1920","appCode":"f002","dzPaySupport":"2","userId":"287214339","city":"%E5%8C%97%E4%BA%AC","utdid":"WVXnflOMWeEDAG79IwDB2QuM","apiVersion":"3.9.7.3069","province":"%E5%8C%97%E4%BA%AC%E5%B8%82","oaid":"","v":"4","afu":"0","imei":"dz_1573548212973","p":"68","clientAgent":"svnVer_1911221445","lsw":"1","apn":"wifi","imsi":"dz_1573548212973","channelFee":"KYY1001760","cmTel":"","sign":"a7ec62bbc4de6d6b3eb280c0c3ef0ed1","pname":"com.ishugui","channelCode":"wb1009710","os":"android23","brand":"Xiaomi","en":"{\"adsdk\":\"2\",\"geyan\":\"1\"}","model":"Redmi Note 4X"},"pri":{"is_single_book":"1","chapter_id":"","book_id":"11000007217"}}

print("请求参数:",json_data)
#可以修改设置参数
json_data['pub']['channelCode']=""
json_data['pub']['pname']="com.ishugui"
json_data['pub']['p']="68"


#可以修改设置接口号
port_inter="244"

print("channelCode:",json_data['pub']['channelCode'])
print("pname:",json_data['pub']['pname'])
print("p:",json_data['pub']['p'])
#josn转换str
json_str=json.dumps(json_data)
#print(json_str)


#判断startswith() 和endswith()
if json_str.startswith("{") and json_str.endswith("}"):
    print('------------以{开头')
    print('------------以}结尾')


#参数
url=baseurl+port_inter+'.do'
querystring=""
payload = json_str
#headers
headers = {
    'Content-Type': "application/json",
    }
#发送请求

print("url:",url)
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

#可以提取参数
print("返回状态：",response.status_code)
print("响应：",response.json())

"""
######--------------------------------------------------------
#序列请求
inter_list=['399','230','231','244','265','368','264','258','242','191','192','236','234']
for i in inter_list:
    port_inter=i
    url=baseurl+port_inter+'.do'

    print('正在请求 %s 接口-----------------------------------'+i)
    print('请求url:%s,\n请求参数：%s'%(url,payload))
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)    
    #可以提取参数
    print("返回状态：",response.status_code)
    print("响应：",response.json())    

"""
#-------------------------------------
#读入文件







