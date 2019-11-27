# -*- coding: utf-8 -*-
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
