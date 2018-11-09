# coding:utf-8
from common import Http
from common import readexcel as reader,writeexcel as writer

srcfile="E:\\myworkspace\\mygit\\mygitworkspace\\autoAPI\\autoTestApi\\datadir\\myapp_Http.xls"
desfile="E:\\myworkspace\\mygit\\mygitworkspace\\autoAPI\\autoTestApi\\datadir\\myHttp_result.xls"

#执行方法
def run(line):
    if line[3]=='post':
        Http.post(line[4],line[5])
        return
    if line[3]=='get':
        Http.get(line[4],line[5])
        return
    if line[3]=='addheader':
        Http.add_header(line[4],line[5])
        return
    if line[3]=='assertequals':
        Http.assert_equals(line[4],line[5])
        return
    if line[3]=='savajson':
        Http.saveJson(line[4],line[5])
        return
    if  line[3]=='seturl':
        Http.seturl(line[4])
        return
    if  line[3]=='settimeout':
        Http.settimeout(line[4])
        return
    if  line[3]=='addparam':
        Http.add_param(line[4],line[5])
        return
    if  line[3]=='removeheader':
        Http.remove_header(line[4])
        return
        
    
                    
reader.open_excel(srcfile)
writer.copy_open(srcfile,desfile)

for i in range(0,reader.r):
    line=reader.readline()
    print(line)
    if len(line[0])>2 or len(line[1])>2:
        #不去执行的行
        pass
    else:
        #执行
        run(line)
                                                        
writer.save_close()

