#_*_coding:utf-8_*_
import os

class FileUtil:

    def __init__(self):
        pass

    @classmethod
    def listdir(cls, path, list_name, exclude_str):  # 传入存储的list
        for f in os.listdir(path):
            file_path = os.path.join(path, f)
            if os.path.isdir(file_path):
                cls.listdir(file_path, list_name, exclude_str)
            else:
                if not exclude_str in file_path:
                    list_name.append(file_path)
					
					
def Listdir(path,list_name,result):
    for f in os.listdir(path):
        file_path=os.path.join(path,f)
        if os.path.isdir(file_path):
            Listdir(file_path,list_name,result)
                
        elif file_path.split('.')[1]=='xlsx' or file_path.split('.')[1]=='xls':            
            if not result in file_path:
                list_name.append(file_path)
    return list_name

#2

def Scan_excel_file(path,result):
    list_name=[]
    listname=Listdir(path,list_name,result)
    '''
    for i in listname:
        print(i)    
    '''
    for file_name in listname:        
        file_name_result=file_name.split('.')[0]+'_result.xls'
        print(file_name,file_name_result)
        if os.path.exists(file_name_result):
            os.remove(file_name_result)
             
    
if __name__=="__main__":
    path="D:\\data"
    list_name=[]
    #1
    names=Listdir(path,list_name,"_result")
    for i in names:
        print(i)
    #2    
    print('-----')    
    Scan_excel_file(path,"_result")
