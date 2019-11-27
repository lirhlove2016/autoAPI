# coding:utf-8
from common.excelutil import ExcelUtil
import requests
import json
import os
import time
# -文件目录配置----------------------------
filepath = os.path.abspath(os.getcwd())
srcfile = os.path.join(filepath, 'datadir/postdata.xlsx')
desfile = os.path.join(filepath, 'datadir/postdata._result.xls')

print(srcfile)


#将str转换为json

#将josn转换为str
print('------------------------------------------------')
a = "{1: 'a', 2: 'b'}"
b = eval(a)
print(type(b),b,type(a),a)


# 获取数据
data, key_names = ExcelUtil.dict_data(srcfile)
reals = []
count = len(data)
print('接口总数', count)
suc_num = 0
for i in range(len(data)):
    print('--正在进行接口测试，开始第%d个请求---------------' % (i + 1))
    datalist = data[i]

    url = "http://" + datalist['url'].strip() + datalist['path'].strip()
    datas = datalist['params']
    timeout = datalist['timeout']
    method = datalist['method']
    headers = {'content-type': datalist['headers']}

    print("-------请求参数-----------------")
    print(method)
    print(url)
    print('header:', headers)
    print('datas', datas)
    print("type(datas)----------------",type(datas))

    #str转换json
    j = json.loads(datas)
    print('j-------------------------------------',j)
    print(type(j))

	#判断startswith() 和endswith()
	if json_str.startswith("{") and json_str.endswith("}"):
	    print('------------以{开头')
	    print('------------以}结尾')

    # json转换str
    json_str = json.dumps(j, ensure_ascii=False)

    print("type(json_str)----------------", type(json_str),json_str)

    # print(json_str)
    print("-------返回参数-----------------")  # 请求接口并打印响应数据
    #url = baseurl + port_inter + '.do'
    querystring = ""
    payload = json_str
    # headers
    headers = {
        'Content-Type': "application/json",
    }
    print("url:--------------", url)
    #response = requests.request("get", url, data=payload, headers=headers, params=querystring)

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    #可以提取参数
    print("返回状态：",response.status_code)
    print("响应：",response.json())






