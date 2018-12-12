#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
version=1.0

'''
by lirh
'''

#设置目录
filepath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
resultDir=os.path.join(filepath,'result')


if __name__=="__main__":
    print(dataDir)
    print(reportDir)
    
