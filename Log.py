import os.path
import Function
import re
import yandere

_log_name = '_log.txt'
png_log_name = 'png_log.txt'

#create_log()

def create_tagslogjpg(tags):
    global _log_name
    file__=open(Function._folder_name+tags+'/'+_log_name,'w')
    file__.write(str(yandere.get_Oldjpgfilename(str(Function.tags_folder(tags)))))
    file__.close()
#    file_.close()

def create_tagslogpng(tags):
    global png_log_name
    file__=open(Function._folder_name+tags+'/'+png_log_name,'w')
    file__.write(str(yandere.get_Oldpngfilename(str(Function.tags_folder(tags)))))
    file__.close()
"""    file_=open(Function._folder_name+tags+'/'+list_name,'w+')
    file_.write(str(Function.tags_folder(tags)))
    file_=open(Function._folder_name+tags+'/'+list_name).read()"""
tags='izumi_tsubasu'

def create_logjpg():
    global _log_name
    file__=open(Function._folder_name+_log_name,'w')
    file__.write(str(yandere.get_Oldjpgfilename(str(Function.page_folder()))))
    file__.close()
#    file_.close()

def create_logpng():
    global png_log_name
    file__=open(Function._folder_name+png_log_name,'w')
    file__.write(str(yandere.get_Oldpngfilename(str(Function.page_folder()))))
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


#print(_tagslogingpng(tags))
