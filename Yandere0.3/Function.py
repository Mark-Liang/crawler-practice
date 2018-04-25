import os.path
import datetime
import hashlib
import re
import os

# 图片存储位置
tagsfolder = 'E:/Yandere2/'
_folder_name = 'E:/Yandere/'

def create_folder():
    global _folder_name
    # 创建目录存放今天爬下来的图
    if not os.path.exists(_folder_name):
        os.makedirs(_folder_name)

def create_tags_folder(tags):
    global tagsfolder
    if not os.path.exists(tagsfolder+tags):
        os.makedirs(tagsfolder+'/'+tags)


def tags_exists(tags:str,file_name:str):
    global tagsfolder
    return os.path.exists(tagsfolder +tags+'/'+ file_name)


def _exists(file_name:str):
    global _folder_name
    return os.path.exists(_folder_name + file_name)

def get_md5(path):
    try:
        md5=hashlib.md5(open(path,'rb').read()).hexdigest()
        return md5
    except:
        print('获取失败')

def clesr():
    os.system('cls')

#path='E:/Yandere2/yano_mitsuki/136545%yano_mitsuki%.jpg'
"""
def _hashlib(path):
    md5=hashlib.md5(path).hexdigest()
    return md5


def get_md5(path):
    file=open(path).read()
    md5=_hashlib(file)
    return md5





#print(get_md5(path))


def tags_folder(tags):
    global _folder_name
    path=[]
    for files in os.walk(_folder_name+tags):
        for file in files:
            Log.tagsopen_add_txt(tags,files)
            return path
#            Log.add(str(path))

print(tags_folder('izumi_tsubasu'))

def page_folder():
    global _folder_name
    _path=[]
    for files in os.walk(_folder_name):
        for file in files:
            _path.append(files)
            return _path

#print(page_folder())




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