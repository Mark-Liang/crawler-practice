import yandere
import urllib.request
import time
import Function
import Log
Function.create_folder()

model=int(input('输入模式:\n 1是按页面下载\n 2是按关键字下载\n :'))
if model==1:
	page=int(input('输入开始页数:'))
	max_page=int(input('输入结束页数:'))
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
