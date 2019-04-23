#!/usr/bin/env python
#coding=utf-8
import os


#app包目录获取
def get_app_filelist(strlj):
    global L
    L = []
    for aaa, bbb, ccc in os.walk(strlj):
        ccc = str(ccc)
        if ccc != '[]':
            ccc = ccc.split(',')
            ccc = list(ccc)
            n = 0
            for CCC in ccc:
                zz = ccc[n].replace("'", "")
                zz = zz.replace("]", "")
                zz = zz.replace("[", "")
                zz = zz.replace(" ", "")
                n = n + 1
                # print(os.path.join(aaa, zz))
                L.append(os.path.join(aaa, zz))			
    return L	

if  __name__=='__main__':
    #示例如下，r是转义\
    l=get_app_filelist(r'F:\download')
    print(L)
