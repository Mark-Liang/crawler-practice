import yandere
import urllib.request
import time
import Function
import addMysql
Function.create_folder()
addMysql.create_database()
#localtime=time.strftime('%Y-%m-%d %H:%M:%S')
#model=int(input('+输入模式:\n 1按页面下载\n 2按关键字下载\n :'))
Function.clesr()
model=1
if model==1:
	#page=int(input('输入开始页数:'))
	#max_page=int(input('输入结束页数:'))
	page=780
	max_page=9000
	while page<=max_page:
		print('正在读取第'+str(page)+'页')
		html=yandere.get_html(page)
		path=Function._folder_name
		for info in yandere.get_list(html):
			files_name=info[3].split('/')[-1]
			file_jpg=info[0]+'.jpg'
			if 'png' in info[2]:
				file_png=info[0]+'.'+info[2]
				if Function._exists(file_jpg)==False and Function._exists(file_png)==False:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_jpg)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()				
					urllib.request.urlretrieve(info[3],path+file_png)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						#print('更新数据库')
				elif Function._exists(file_jpg)==False and Function._exists(file_png)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的png格式已存在，跳过')
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_jpg)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')	
					jpg_md5=Function.get_md5(path+file_jpg)				
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						#print('更新数据库')
				elif Function._exists(file_png)==False and Function._exists(file_jpg)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的jpg格式已存在，跳过')
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()				
					urllib.request.urlretrieve(info[3],path+file_png)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						#print('更新数据库')
				elif Function._exists(file_jpg)==True and Function._exists(file_png)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的jpg格式已存在，跳过')
					print(info[0]+'的png格式已存在，跳过')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						#print('更新数据库')
			else:
				#print('编号'+info[0]+'并没PNG格式')
				localtime=time.strftime('%Y-%m-%d %H:%M:%S')
				file_name=info[0]+'.'+info[2]
				if Function._exists(file_name):
					print(info[0]+'的jpg格式已存在，跳过')
					jpg_md5=Function.get_md5(path+file_jpg)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,info[0])
						#print('更新数据库')
					continue
				else:
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
						#print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,info[0])
						#print('更新数据库')
		page+=1
elif model==2:
	#tags=input('输入关键字(区分大小写):')
	tags='izumi_tsubasu'
	Function.create_tags_folder(tags)
	#page=1
	if not yandere.get_lastpage(yandere.get_htmltags(tags)):
		print ('此tags只有一页')
	else:
		last_page=yandere.get_lastpage(yandere.get_htmltags(tags))[0]
		print('此tags的max值为'+str(last_page)+'页')
	#page=int(input('输入开始页数:'))
	#max_page=int(input('输入结束页数:'))
	path=Function._folder_name+tags+'/'
	while page<=max_page:
		print('正在读取第'+str(page)+'页')
		html=yandere.get_htmltags(tags,page)
		for info in yandere.get_list(html):
			files_name=info[3].split('/')[-1]
			file_jpg=info[0]+'%'+tags+'%'+'.jpg'
			if 'png' in info[2]:
				file_png=info[0]+'%'+tags+'%'+'.'+info[2]
				if Function.tags_exists(tags,file_jpg)==False and Function.tags_exists(tags,file_png)==False:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_jpg)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()				
					urllib.request.urlretrieve(info[3],path+file_png)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						print('更新数据库')
				elif Function.tags_exists(tags,file_jpg)==False and Function.tags_exists(tags,file_png)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的png格式已存在，跳过')
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_jpg)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')	
					jpg_md5=Function.get_md5(path+file_jpg)				
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						print('更新数据库')
				elif Function.tags_exists(tags,file_png)==False and Function.tags_exists(tags,file_jpg)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的jpg格式已存在，跳过')
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()				
					urllib.request.urlretrieve(info[3],path+file_png)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						print('更新数据库')
				elif Function.tags_exists(tags,file_jpg)==True and Function.tags_exists(tags,file_png)==True:
					localtime=time.strftime('%Y-%m-%d %H:%M:%S')
					print(info[0]+'的jpg格式已存在，跳过')
					print(info[0]+'的png格式已存在，跳过')
					jpg_md5=Function.get_md5(path+file_jpg)
					png_md5=Function.get_md5(path+file_png)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#post=info[0]
					sqlpost=addMysql.select_post(info[0])
					#print(sqlpost)
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,1,path+file_png,jpg_md5,png_md5,localtime,info[0])
						print('更新数据库')
			else:
				#print('编号'+info[0]+'并没PNG格式')
				localtime=time.strftime('%Y-%m-%d %H:%M:%S')
				file_name=info[0]+'%'+tags+'%'+'.'+info[2]
				if Function.tags_exists(tags,file_name):
					print(info[0]+'的jpg格式已存在，跳过')
					jpg_md5=Function.get_md5(path+file_jpg)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,info[0])
						print('更新数据库')
					continue
				else:
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
					jpg_md5=Function.get_md5(path+file_jpg)
					rename=files_name.split('.')[-2]
					tags_name=rename.replace('%20',',')[3:]
					#addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
					sqlpost=addMysql.select_post(info[0])
					if sqlpost==None:
						addMysql.add_database(info[0],tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,localtime,1)
						print('写入数据库')
					else:
						addMysql.updata_database(tags_name,path+file_jpg,0,'',jpg_md5,'',localtime,info[0])
						print('更新数据库')
		page+=1
print('下载完毕')

#(addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addupdata_time,addpost)

"""				file_name=info[0]+'%'+tags+'%'+'.'+info[2]
				if Function.tags_exists(tags,file_name):
					print(info[0]+'的PNG格式已存在，跳过')
					continue
				else:
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()				
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
				file_name=info[0]+'%'+tags+'%'+'.jpg'
				if Function.tags_exists(tags,file_name):
					print(info[0]+'的jpg格式已存在，跳过')
					continue
				else:
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')"""



"""Function.create_folder()

model=int(input('输入模式:\n 1按页面下载\n 2按关键字下载\n :'))
if model==1:
	page=int(input('输入开始页数:'))
	max_page=int(input('输入结束页数:'))
	Log.page_folder()
	pos=1
	Log.create_logjpg()
	Log.create_logpng()
	while page<=max_page:
		print('正在读取第'+str(page)+'页')
		html=yandere.get_html(page)
		png_img=Log._tagslogingpng(tags)
		jpg_img=Log._tagslogingjpg(tags)
		path=Function._folder_name
		for info in yandere.get_list(html):

			if 'png' in info[2]:
				if info[0] in png_img:
					print('该图片已存在，跳过')
					continue
				else:
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()
					file_name=info[3].split('/')[-1]
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
				if info[0] in jpg_img:
					print('该图片已存在，跳过')
					continue
				else:
					file_name=info[4].split('/')[-1]
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
				pos+=1
			else:
				#print('编号'+info[0]+'并没PNG格式')
				if info[0] in jpg_img:
					print('该图片已存在，跳过')
					continue
				else:
					file_name=info[3].split('/')[-1]
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')

		page+=1
	Log.DELETE_log()
elif model==2:
	tags=input('输入关键字(区分大小写):')
	Function.create_tags_folder(tags)
	Log.tags_folder(tags)
	page=1
	if not yandere.get_lastpage(yandere.get_htmltags(tags)):
		print ('此tags只有一页')
	else:
		last_page=yandere.get_lastpage(yandere.get_htmltags(tags))[0]
		print('此tags的max值为'+str(last_page)+'页')
	page=int(input('输入开始页数:'))
	max_page=int(input('输入结束页数:'))
	Log.create_tagslogjpg(tags)
	Log.create_tagslogpng(tags)
	path=Function._folder_name+tags+'/'
	while page<=max_page:
		print('正在读取第'+str(page)+'页')
		html=yandere.get_htmltags(tags,page)
		png_img=Log._tagslogingpng(tags)
		jpg_img=Log._tagslogingjpg(tags)
		for info in yandere.get_list(html):

			if 'png' in info[2]:
				if info[0] in png_img:
					print('该图片已存在，跳过')
					continue
				else:
					print('正在下载编号为'+info[0]+'的PNG格式')
					ts = time.time()
					file_name=info[3].split('/')[-1]
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
				if info[0] in jpg_img:
					print('该图片已存在，跳过')
					continue
				else:
					file_name=info[4].split('/')[-1]
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[4],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
				pos+=1
			else:
				#print('编号'+info[0]+'并没PNG格式')
				if info[0] in jpg_img:
					print('该图片已存在，跳过')
					continue
				else:
					file_name=info[3].split('/')[-1]
					print('正在下载编号为'+info[0]+'的jpg格式')
					ts = time.time()
					urllib.request.urlretrieve(info[3],path+file_name)
					print('下载完毕。耗时：'+str(int(time.time() - ts))+'s')
		page+=1
	Log.DELETE_tag_log(tags)

print('下载完毕')"""
