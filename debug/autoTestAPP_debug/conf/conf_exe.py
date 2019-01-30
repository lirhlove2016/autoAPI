import os
import sys

#exe文件运行目录
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
    
filepath=application_path
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
