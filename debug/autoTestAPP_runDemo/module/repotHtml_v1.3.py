# -*- coding=utf-8 -*-
import  time,os

"""
V1.2
1.生成total表格
2.生成report表格
3.生成modulelist表格
4.生成module表格
5.生成case表格
6.

"""
#----数据部分-------------------------------------------
func_dict={"funcname":"模块1",}

funcname=['书架','书城','分类','我的']
modulelist1={"name":"业务模块1","total":"30","passnum":"25","failnum":"0","radio":"80","status":"PASS"}
modulelist2={"name":"业务模块2","total":"10","passnum":"10","failnum":"0","radio":"80","status":"PASS"}

case1={"name":"模块1","total":"10","passnum":"10","failnum":"0","radio":"80","status":"PASS"}
case2={"name":"模块2","total":"20","passnum":"15","failnum":"5","radio":"75","status":"Fail"}

VERSION_DICT={"version": '快看小说 3.8.8',"radio":'99',"runstarttime":time.strftime('%Y-%m-%d %H:%M:%S'),"runstoptime" : time.strftime('%Y-%m-%d %H:%M:%S')}

#---END-------------------------------------------

caselist=[]
modulelist=[]
modulelist.append(modulelist1)
modulelist.append(modulelist2)
print(modulelist)

for i in range(len(modulelist)):
    pass
    #print('业务模块list',modulelist[i])

caselist.append(case1)
caselist.append(case2)
print(caselist)
for i in range(len(caselist)):
    pass
    #print('case list',caselist[i])


class Template_mixin(object):
    """html报告"""
    # ------------------------------------------------------------------------
    # HTML Template    
    HTML_TMPL = r"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>%(title)s</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h2 style="font-family: Microsoft YaHei">%(title)s</h2>

            <p class='attribute'><strong>测试结果 : </strong> %(total)s</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        </style>
        </head>
        <body>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                    <col align='left' />
                    <col align='right' />
                    <col align='right' />
                    <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th>客户端及版本</th>
                    <th>通过率</th>
                    <th>开始时间</th>
                    <th>结束时间</th>
                </tr>
                %(table_total)s
        
            </table>
            <!-- 执行模块 -->
            <p class='attribute'><strong>测试报告详情 : </strong> </p>
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                   <col align='left' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th colspan="2">功能模块</th>
                    <th>用例总数</th>
                    <th>通过数</th>
                    <th>状态</th>
                </tr>
                %(table_modulelist)s
                %(table_caselist)s
               
            </table>
            <script type="text/javascript">
                //change color
                //取都用demo的多组
                var eles = document.getElementsByClassName('demo');
                console.log(eles);
                //var x=document.getElementById("demo").innerText;
                //console.log("the value is :"+x);
                //每组都应用样式
                for(var i = 0; i < eles.length; i++){
                    if(eles[i].innerText == 'PASS'){
                        eles[i].style.color = 'green';
                    }else{
                        eles[i].style.color = 'red';
                    }
                }

            </script>   

        </body>
        </html>"""
    # variables: (title,total, table_total,table_module,table_case)
    # ------------------------------------------------------------------------
    # Report

    #总数据
    REPORT_TMPL_TOTAL = """
        <tr class='failClass warning'>
            <td>%(version)s</td>
            <td>%(radio)s</td>
            <td>%(runstarttime)s</td>
            <td>%(runstoptime)s</td>
        </tr>"""
  
    #report表头
    #report表module list
    REPORT_TMPL_MODULE_LIST = """
        <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th colspan="2">%(module)s</th>
            <th>%(casetotal)s</th>
            <th>%(passtotal)s</th>
            <th class='demo' id="demo">%(status)s</th>
        </tr>"""

    #reprot表格module模块
    REPORT_TMPL_MODULE = """
        <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th>%(name)s</th>
            <th>%(module)s</th>
            <th>%(casetotal)s</th>
            <th>%(passtotal)s</th>
            <th class='demo' id="demo">%(status)s</th>
        </tr>"""

    #case list数据        
    REPORT_TMPL_CASE = """
        <tr class='failClass warning'>
            <td>%(name)s</td>
            <td>%(module)s</td>
            <td>%(casetotal)s</td>
            <td>%(passtotal)s</td>
            <td class='demo'  id="demo2">%(status)s</td>
        </tr>"""
            
def  run(title,value,version,moduellist1,case1,case2):
    table_tr0=""
    table_tr1=""
    table_ca1=""
    table_ca2=""

    html = Template_mixin()  
    #title
    title_str=title
    #表头总数
    total_str = value

    #总表数据
    table_td = html.REPORT_TMPL_TOTAL % dict(version=VERSION_DICT['version'],radio=VERSION_DICT['radio'],runstarttime=VERSION_DICT['runstarttime'],runstoptime = VERSION_DICT['runstoptime'])
    table_tr0 += table_td

    #详情数据
    table_td_module=html.REPORT_TMPL_MODULE_LIST % dict(
        module=modulelist1["name"],
        casetotal=modulelist1["total"],
        passtotal=modulelist1["passnum"],
        status=modulelist1["status"],
        )
    table_tr1 += table_td_module
  
    #case数据
    table_td_case1=html.REPORT_TMPL_CASE % dict(
        name="",
        module=case1["name"],
        casetotal=case1["total"],
        passtotal=case1["passnum"],
        status=case1["status"],
        )
    table_ca1 += table_td_case1    
    
    table_td_case2=html.REPORT_TMPL_CASE % dict(
        name="",
        module=case2["name"],
        casetotal=case2["total"],
        passtotal=case2["passnum"],
        status=case2["status"],
        )
    table_ca2 += table_td_case2

    output=html.HTML_TMPL % dict(
        title=title_str,
        total = total_str,
        table_total = table_tr0,
        table_modulelist=table_td_module,
        table_caselist=table_ca1,
        )

    # 生成html报告
    filename='{date}_TestReport.html'.format(date=time.strftime('%Y%m%d%H%M%S'))
 
    print(filename)
    #获取report的路径
    dir= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report/html')
    filename=os.path.join(dir,filename)
 
    with open(filename, 'wb') as f:
        f.write(output.encode('utf8'))    

def generate_report(modulelist1, caselist):
    rows = []

    #module 加入rows
    row = REPORT_TMPL_MODULE_LIST % dict(
        module=modulelist1["name"],
        casetotal=modulelist1["total"],
        passtotal=modulelist1["passnum"],
        status=modulelist1["status"],
        )
    rows.append(row)

    table_tr1 += table_td_module
  
    for i in  caselist:
        case_name=caselist[i]["name"]
        case_total=caselist[i]["total"]
        case_passnum=caselist[i]["passnum"]
        case_status=caselist[i]["status"]
        #case 加入rows
        row=EPORT_TMPL_CASE % dict(
            name="",
            module=case_name,
            casetotal=case_total,
            passtotal=case_passnum,
            status=case_status,
        )
        rows.append(row)


if __name__ == '__main__':
    table_tr0 = ''
    table_tr1=""
    table_ca1=""
    table_ca2=""    
    numfail = 1
    numsucc = 9

    #title
    title="自动化测试报告"
    #表头总数
    value = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)


    run(title,value,VERSION_DICT,modulelist1,case1,case2)


