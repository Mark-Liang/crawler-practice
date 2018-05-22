import os.path
import datetime
import hashlib
import re
import os
from PIL import Image
import glob
import urllib.request
import time
import socket

tagsfolder = 'E:/Yandere2/'
_folder_name = 'F:/Yandere/'
thumbnail='F:/Yandere/thumbnail/'
Image.MAX_IMAGE_PIXELS = 1000000000
def create_folder():
    global _folder_name
    if not os.path.exists(_folder_name):
        os.makedirs(_folder_name)

def create_thumbnailfolder():
    global thumbnail
    if not os.path.exists(thumbnail):
        os.makedirs(thumbnail)



def create_fol(post):
    global _folder_name
    name=str(post)
    if len(name)>4:
        folname=name[:-4]
        folname=folname
        if not os.path.exists(_folder_name+folname+'/'):
            os.makedirs(_folder_name+folname+'/')
        return str(_folder_name+folname+'/')
    else:
        folname=name[:-4]
        folname=folname+'0'
        if not os.path.exists(_folder_name+folname+'/'):
            os.makedirs(_folder_name+folname+'/')
        return str(_folder_name+folname+'/')


def create_tags_folder(tags):
    global tagsfolder
    if not os.path.exists(tagsfolder+tags):
        os.makedirs(tagsfolder+'/'+tags)


def tags_exists(tags:str,file_name:str):
    global tagsfolder
    return os.path.exists(tagsfolder +tags+'/'+ file_name)


def _exists(path,file_name:str):
    return os.path.exists(path + file_name)

def get_md5(path):
    try:
        md5=hashlib.md5(open(path,'rb').read()).hexdigest()
        return md5
    except:
        print('获取失败')

def get_tags_name(full):
    rename=re.sub(r"(yande.re%20\d+%20)",'',full)
    tags_name=re.sub(r"(.png|.jpg)",'',rename)
    return tags_name

def clesr():
    os.system('cls')



def get_size(path):
    try:
        img=Image.open(path)
        return img.size
    except:
        pass



def dl(url,path):
    try:
        urllib.request.urlretrieve(url,path)
    except:
        count=1
        while count<=10:
            try:
                urllib.request.urlretrieve(url,path)
                break
            except:
                print('失败重试')
                count+=1
        if count > 10:
            print("下载失败")



def jpg_dl(post,url,path):
    socket.setdefaulttimeout(500)
    try:
        print('正在下载编号为'+str(post)+'的jpg格式')
        ts = time.time()
        dl(url,path)
        print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
    except socket.timeout:
        count=1
        while count<=10:
            try:
                print('下载失败,重试')
                print('正在下载编号为'+str(post)+'的jpg格式')
                ts = time.time()
                dl(url,path)
                print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
                break
            except socket.timeout:
                print('第'+str(count)+'次重试')
                count += 1
        if count > 10:
            print("下载失败")

def png_dl(post,url,path):
    socket.setdefaulttimeout(500)
    try:
        print('正在下载编号为'+str(post)+'的png格式')
        ts = time.time()
        dl(url,path)
        print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
    except socket.timeout:
        count=1
        while count<=10:
            try:
                print('下载失败,重试')
                print('正在下载编号为'+str(post)+'的png格式')
                ts = time.time()
                dl(url,path)
                print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
                break
            except socket.timeout:
                print('第'+str(count)+'次重试')
                count += 1
        if count > 10:
            print("下载失败")

def get_thumbnail(path,post,url):
    global thumbnail
    try:
        img=Image.open(path)
        img.thumbnail((300,300))
        img.save(thumbnail+str(post)+'.jpg')
    except:
        jpg_dl(post,url,path)
        img=Image.open(path)
        img.thumbnail((300,300))
        img.save(thumbnail+str(post)+'.jpg')

def is_(path,url,post):
    try:
        im=Image.open(path)
        im.thumbnail((300,300))
    except:
        png_dl(post,url,path)

