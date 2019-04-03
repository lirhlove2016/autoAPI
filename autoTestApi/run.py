# coding:utf-8
import json
import unittest
import time
import os
from common.excel import ExcelUtil
from common.Api_request import ApiRequest 
from common import HTMLTestRunner
from common.listdir import Listdir,Scan_excel_file
from conf.conf import dataDir,reportDir,TIMEOUT,TOKEN
from conf.conf import API_ENV,API_ENV_ON,API_ENV_NOW
from common.dataUtil import DataUtil

class testAPI(unittest.TestCase):

    #：scan
    def test_scan_datafiles(self):
        datafilepath=dataDir
        list_name=[]
        listname=Listdir(datafilepath,list_name,'_result')
        '''
        for i in listname:
            print(i)    
        '''
        for file_name in listname:        
            file_name_result=file_name.split('.')[0]+'_result.xlsx'
            print(file_name,file_name_result)
            if os.path.exists(file_name_result):
                os.remove(file_name_result)

            #获取数据
            data,key_names= ExcelUtil(file_name).dict_data()
            #print(key_names)
            reals=[]
            count=len(data)
            print('接口总数',count)
            suc_num=0
            for i in range(len(data)):
                print('--正在进行接口测试，开始第%d个请求---------------'%(i+1))
                datalist=[]    
                datalist=data[i]
                #url读数据
                url=datalist['url'].strip()
                url=DataUtil.get_url(url) #url
                url="http://"+url+ datalist['path'].strip()
                datas=datalist['params']
                method=datalist['method']
                headers={}
                headers['content-type']=datalist['headers']
                #token处理
                if datalist['tokenname']=='BDHAuthorization':
                    tokenname=datalist['tokenname']
                    headers[tokenname]=datalist['token']
                else:
                    tokenname=datalist["tokenname"]
                    token=datalist['token']
                    location=""
                    if len(token)<10:
                        tokenname,token,location=DataUtil.get_token(tokenname,token)

                        if location=='param':
                            datas=datas+"""&"""+tokenname+"""="""+token
                
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
            ExcelUtil.write_excel(file_name_result,reals,key_names)

    #
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
            url=datalist['url'].strip()               
            url="http://"+url+ datalist['path'].strip()
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
    #unittest.main()
    print(dataDir,reportDir)
    #
    suite = unittest.TestSuite()
    #suite.addTest(testAPI('test_bdh_api'))
    suite.addTest(testAPI('test_scan_datafiles'))
    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))           
    htmlreport = reportDir+r"/"+now+"_result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    runner.run(suite)
    fp.close()

    

    
    
