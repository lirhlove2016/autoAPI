# -*- coding=utf-8 -*-
#
import  time,os
 
 
class Template_mixin(object):
    """html报告"""
    HTML_TMPL = r"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>自动化测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h1 style="font-family: Microsoft YaHei">自动化测试报告</h1>
            <p class='attribute'><strong>测试结果 : </strong> %(value)s</p>
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
                    <th>版本</th>
                    <th>操作步骤</th>
                    <th>用例执行结果</th>
                    <th>操作时间</th>
                </tr>
                %(table_tr)s
            </table>
        </body>
        </html>"""
 
    TABLE_TMPL = """
        <tr class='failClass warning'>
            <td>%(version)s</td>
            <td>%(step)s</td>
            <td>%(runresult)s</td>
            <td>%(runtime)s</td>
        </tr>"""
 
 
if __name__ == '__main__':
    table_tr0 = ''
    numfail = 1
    numsucc = 9
    html = Template_mixin()
    
    table_td = html.TABLE_TMPL % dict(version = '3.8.8',step='输入正确的用户名，密码进行登录',runresult='登录成功',runtime = time.strftime('%Y-%m-%d %H:%M:%S'),)
    table_tr0 += table_td
    total_str = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)
    output = html.HTML_TMPL % dict(value = total_str,table_tr = table_tr0,)
    #print('output',output)
    # 生成html报告
    filename='{date}_TestReport.html'.format(date=time.strftime('%Y%m%d%H%M%S'))
 
    print(filename)
    #获取report的路径
    dir= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report')
    filename=os.path.join(dir,filename)
 
 
    with open(filename, 'wb') as f:
        f.write(output.encode('utf8'))
