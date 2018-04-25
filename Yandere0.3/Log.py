
import Function
import re
import yandere
import os
import os.path
list_name='list_.txt'
_log_name = '_log.txt'
png_log_name = 'png_log.txt'
tags='izumi_tsubasu'




#create_log()

def tagsopen_add_txt(tags,data):
    a=open(Function._folder_name+tags+'/'+list_name,'a+')
    a.write(str(data))
    a.close()

def open_add_txt(data):
    a=open(Function._folder_name+list_name,'a+')
    a.write(str(data))
    a.close()



def tags_folder(tags):
    for files in os.walk(Function._folder_name+tags):
        for file in files:
            tagsopen_add_txt(tags,files)

#            Log.add(str(path))

#print(tags_folder('izumi_tsubasu'))

def page_folder():
    global _folder_name
    for files in os.walk(Function._folder_name):
        for file in files:
            open_add_txt(files)

def create_tagslogjpg(tags):
    global _log_name
    file_=open(Function._folder_name+tags+'/'+list_name).read()
    file__=open(Function._folder_name+tags+'/'+_log_name,'w+')
    file__.write(str(yandere.get_Oldjpgfilename(file_)))
    file__.close()
#    file_.close()


def create_tagslogpng(tags):
    global png_log_name
    file_=open(Function._folder_name+tags+'/'+list_name).read()
    file__=open(Function._folder_name+tags+'/'+png_log_name,'w+')
#    print(yandere.get_Oldpngfilename(file_))
    file__.write(str(yandere.get_Oldpngfilename(file_)))
    file__.close()




def create_logjpg():
    global _log_name
    file_=open(Function._folder_name+list_name).read()
    file__=open(Function._folder_name+_log_name,'w+')
    file__.write(yandere.get_Oldjpgfilename(str(file_)))
    file__.close()

def create_logpng():
    global png_log_name
    file_=open(Function._folder_name+list_name).read()
    file__=open(Function._folder_name+png_log_name,'w+')
    file__.write(yandere.get_Oldpngfilename(str(file_)))
    file__.close()



def _logingpng():
    file_=open(Function._folder_name+png_log_name).read()
    return file_

def _logingjpg():
    file_=open(Function._folder_name+_log_name).read()
    return file_

def _tagslogingjpg(tags):
    file_=open(Function._folder_name+tags+'/'+_log_name).read()
    return file_

def _tagslogingpng(tags):
    file_=open(Function._folder_name+tags+'/'+png_log_name).read()
    return file_

def DELETE_log():
    os.remove(Function._folder_name+png_log_name)
    os.remove(Function._folder_name+_log_name)


def DELETE_tag_log(tags):
    os.remove(Function._folder_name+tags+'/'+png_log_name)
    os.remove(Function._folder_name+tags+'/'+_log_name)


def changefilename():
    path='E:/Yandere/'
    path1='E:/Yandere2/new/'
    files=os.listdir(path)
    for filename in files:
        portion=filename.split('%20')[1]
        print(portion)
        if Function._exists(path1+portion+'.jpg')==False:
            os.renames(path+filename,path1+portion+'.jpg')
            #os.remove(path+filename)
        else:
            continue



def changfilename2():
    path='E:/Yandere/'
    path1='E:/Yandere2/2/1/2/new/'
    files=os.listdir(path)
    for filename in files:
        if _exists('E:/Yandere2/new'+filename)==False:
            open_add_txt(files)
        else:
            continue

"""
        md5=Function.get_md5(path+filename)
        print(md5)
"""
changefilename()


#create_tagslogpng(tags)
#create_tagslogjpg(tags)
#print(_tagslogingpng(tags))

