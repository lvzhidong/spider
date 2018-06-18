#! user/bin/env python3
# -*- coding:utf-8 -*-

# 用于获取指定文件夹里的所有文件路径，包含子文件夹里的

import os


class Directory(object):
    def __init__(self, target_path):
        self.__path = target_path  # 把这个类变量设为私有变量，外部不能访问

    def getAllFiles(self, path=None):
        if path is None:
            path = self.__path
        for file in os.listdir(path):
            filePath = os.path.join(path, file)
            # print(filePath)
            if os.path.isfile(filePath):
                print(filePath)
            else:
                self.getAllFiles(filePath)

    def get_class_name(self):
        print("class name is : %s")




myDir = Directory(r"C:\Users\zhidong\PycharmProjects\exercise\github\spider")

# myDir.getAllFiles()
# print(myDir.getAllFiles.__name__)

def test(Directory):
    Directory.get_class_name()


test(myDir)