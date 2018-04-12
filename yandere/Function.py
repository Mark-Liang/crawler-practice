import os.path
import datetime
import hashlib
import re
# 图片存储位置
_folder_name = 'E:/Yandere2/'


def create_folder():
    global _folder_name
    # 创建目录存放今天爬下来的图
    if not os.path.exists(_folder_name):
        os.makedirs(_folder_name)

def create_tags_folder(tags):
    global _folder_name
    if not os.path.exists(_folder_name+tags):
        os.makedirs(_folder_name+'/'+tags)


def tags_folder(tags):
    global _folder_name
    path=[]
    for root,dirs,files in os.walk(_folder_name+tags):
        for file in files:
            path.append(files)
            return path
#            Log.add(str(path))

#print(tags_folder('izumi_tsubasu'))

def page_folder():
    global _folder_name
    _path=[]
    for root,dirs,files in os.walk(_folder_name):
        for file in files:
            _path.append(files)
            return _path

#print(page_folder())


"""

def get_md5(file_name):
    md5=hashlib.md5(file_name).read().hexdigest()
    return md5

def write(file_name: str,data, root: bool = False):

    写出文件d
    :param file_name: 文件名
    :param data: 文件数据
    :param root: 是否写到根目录
    :return:

    global _folder_name
    file_name = file_name if root else _folder_name + '/' + file_name  # 类似三元运算符
    file = open(file_name, 'wb')
    if isinstance(data, int) or isinstance(data, str):
        data = str(data).encode()
    file.write(data)
    file.close()


def get(file_name: str):

    获取文件内容
    :param file_name: 文件名
    :return: str

    file = open(file_name)
    data = file.readline()
    file.close()
    return data
"""