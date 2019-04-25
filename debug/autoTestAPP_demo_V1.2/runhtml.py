# coding:utf-8
import json
import unittest
import time
import os
from common.readexcel import ExcelUtil
from common.Api_request import ApiRequest 
import conf
from common import HTMLTestRunner
from common.writeexcel import write_excel

testxlsx = r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\myapidata.xlsx"
testxlsx=conf.testxlsx
newfile=conf.newfile
#print('test',testxlsx,newfile)

#report
curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")


class testAPI(unittest.TestCase):

    def test_bdh_api(self):
        #获取数据
        data,key_names= ExcelUtil(testxlsx).dict_data()
        #print(key_names)
        reals=[]
        count=len(data)
        print('接口总数',count)
        suc_num=0
        for i in range(len(data)):
            print('--正在进行接口测试，开始第%d个请求---------------'%(i+1))
            datalist=[]    
            datalist=data[i]
            
            url="http://"+datalist['url'].strip()+ datalist['path'].strip()
            datas=datalist['params']
            method=datalist['method']
            headers={}
            headers['content-type']=datalist['headers']
            if datalist['tokenname']=='BDHAuthorization':
                tokenname=datalist['tokenname']
                headers[tokenname]=datalist['token']
            print("-------请求参数-----------------") 
            print(method)
            print(url)
            print('header:',headers)
            print('data',datas)

            print("-------返回参数-----------------") 
            my_request=ApiRequest(method,url,datas,headers)
            r=my_request.api_request()

            print('code',my_request.get_code())
            print('response',r.json())
            res=r.json()
            datalist['realresult']=str(r.json())
            #期望结果
            ex_result=datalist['expectedresult']
            AC_result=datalist['realresult']
            
            if ex_result in AC_result:
                print('第{0}个接口，{1}:测试成功。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                datalist['result']='测试成功'
                suc_num=suc_num+1
            else:
                print('第{0}个接口，{1}:测试失败。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                datalist['result']='测试失败'

            #保存所有数据
            reals.append(datalist)
        
        #write_datas
        print("-------正在写入数据，请等待-----------------") 
        write_excel(newfile,reals,key_names)
        return suc_num,reals,key_names

                
    
if __name__=="__main__":

    suite = unittest.TestSuite()
    suite.addTest(testAPI('test_bdh_api'))
    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))           
    htmlreport = report_path+r"/"+now+"_result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    runner.run(suite)
    fp.close()

    

    
    
