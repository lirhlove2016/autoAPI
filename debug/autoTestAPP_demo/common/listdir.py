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
            elif file_path.split('.')[1]=='xlsx' or file_path.split('.')[1]=='xls':
                if not exclude_str in file_path:
                    list_name.append(file_path)					
    
if __name__=="__main__":
    pas

