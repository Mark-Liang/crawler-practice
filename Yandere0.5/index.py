import yandere
import time
import Function
import addMysql
Function.create_folder()
addMysql.create_database()
Function.create_thumbnailfolder()
Function.clesr()
model=int(input('输入模式:\n 1按页面下载 2按关键字下载 \n :'))
Function.clesr()
if model==1:
    page=int(input('输入开始页数:'))
    max_page=int(input('输入结束页数:'))
    while page<=max_page:
        print('正在读取第'+str(page)+'页')
        html=yandere.get_html(page)
        for info in yandere.get_list(html):
            path=Function.create_fol(info[0])
            localtime=time.strftime('%Y-%m-%d %H:%M:%S')
            files_name=info[3].split('/')[-1]
            file_jpg=info[0]+'.jpg'
            if 'png' in info[2]:
                file_png=info[0]+'.'+info[2]
                if Function._exists(path,file_jpg)==False and Function._exists(path,file_png)==False:
                    Function.png_dl(info[0],info[3],path+file_png)
                    Function.jpg_dl(info[0],info[4],path+file_jpg)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,info[0])
                elif Function._exists(path,file_jpg)==False and Function._exists(path,file_png)==True:
                    print(info[0]+'的png格式已存在，跳过')
                    Function.jpg_dl(info[0],info[4],path+file_jpg)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)             
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,info[0])
                elif Function._exists(path,file_png)==False and Function._exists(path,file_jpg)==True:
                    print(info[0]+'的jpg格式已存在，跳过')
                    Function.png_dl(info[0],info[3],path+file_png)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,info[0])
                elif Function._exists(path,file_jpg)==True and Function._exists(path,file_png)==True:
                    print(info[0]+'的jpg格式已存在，跳过')
                    print(info[0]+'的png格式已存在，跳过')
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,info[0])
            else:
                file_name=info[0]+'.'+info[2]
                if Function._exists(path,file_name):
                    print(info[0]+'的jpg格式已存在，跳过')
                    jpg_md5=Function.get_md5(path+file_jpg)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    jpg_size=Function.get_size(path+file_jpg)
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,info[0])
                    continue
                else:
                    Function.jpg_dl(info[0],info[3],path+file_jpg)
                    jpg_md5=Function.get_md5(path+file_jpg)
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    jpg_size=Function.get_size(path+file_jpg)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,info[0])
        page+=1
elif model==2:
    tags=input('输入关键字(区分大小写):')
    Function.create_tags_folder(tags)
    page=1
    if not yandere.get_lastpage(yandere.get_htmltags(tags)):
        print ('此tags只有一页')
    else:
        last_page=yandere.get_lastpage(yandere.get_htmltags(tags))[0]
        print('此tags的max值为'+str(last_page)+'页')
    page=int(input('输入开始页数:'))
    max_page=int(input('输入结束页数:'))
    path=Function.tagsfolder+tags+'/'
    while page<=max_page:
        print('正在读取第'+str(page)+'页')
        html=yandere.get_htmltags(tags,page)
        for info in yandere.get_list(html):
            files_name=info[3].split('/')[-1]
            file_jpg=info[0]+'.jpg'
            localtime=time.strftime('%Y-%m-%d %H:%M:%S')
            if 'png' in info[2]:
                file_png=info[0]+'.'+info[2]
                if Function.tags_exists(tags,file_jpg)==False and Function.tags_exists(tags,file_png)==False:
                    Function.png_dl(info[0],info[3],path+file_png)
                    Function.jpg_dl(info[0],info[4],path+file_jpg)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass
                elif Function.tags_exists(tags,file_jpg)==False and Function.tags_exists(tags,file_png)==True:
                    print(info[0]+'的png格式已存在，跳过')
                    Function.jpg_dl(info[0],info[4],path+file_jpg)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)             
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass
                elif Function.tags_exists(tags,file_png)==False and Function.tags_exists(tags,file_jpg)==True:
                    print(info[0]+'的jpg格式已存在，跳过')
                    Function.png_dl(info[0],info[3],path+file_png)
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass
                elif Function.tags_exists(tags,file_jpg)==True and Function.tags_exists(tags,file_png)==True:
                    print(info[0]+'的jpg格式已存在，跳过')
                    print(info[0]+'的png格式已存在，跳过')
                    Function.is_(path+file_png,info[3],info[0])
                    jpg_md5=Function.get_md5(path+file_jpg)
                    png_md5=Function.get_md5(path+file_png)
                    jpg_size=Function.get_size(path+file_jpg)
                    png_size=Function.get_size(path+file_png)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,jpg_size[0],jpg_size[1],png_size[0],png_size[1],Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass
            else:
                file_name=info[0]+'.'+info[2]
                if Function.tags_exists(tags,file_name):
                    print(info[0]+'的jpg格式已存在，跳过')
                    jpg_md5=Function.get_md5(path+file_jpg)
                    jpg_size=Function.get_size(path+file_jpg)
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass
                else:
                    Function.jpg_dl(info[0],info[3],path+file_jpg)
                    jpg_md5=Function.get_md5(path+file_jpg)
                    jpg_size=Function.get_size(path+file_jpg)
                    tags_name=Function.get_tags_name(info[3].split('/')[-1])
                    Function.get_thumbnail(path+file_jpg,info[0],info[4])
                    sqlpost=addMysql.select_post(info[0])
                    if sqlpost==None:
                        addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',jpg_size[0],jpg_size[1],0,0,Function.thumbnail+file_jpg,localtime,localtime,1)
                    else:
                        pass

        page+=1
print('下载完毕')