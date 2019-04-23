#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
version=1.0

'''
by lirh
'''

#设置目录
filepath=r"E:\download"


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
    
filepath=os.path.dirname(application_path)

dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')



if __name__=="__main__":
    print(dataDir)
    print(reportDir)

    print(os.path.dirname(sys.executable))
    print(os.path.dirname(__file__))
    conf=os.path.dirname(__file__)
    f=os.path.dirname(conf)
    
    ff=os.path.abspath(f)

    print(conf,f,ff)
    

    

    
