import urllib.request
import re
import Http

#import Log
#t='https://konachan.com'
def get_html(page=1):
	url='https://yande.re/post?page='+str(page)
	html=Http.get_Source(url).decode('utf-8')
	return html
"""
获取源码
"""
def get_list(html:str):
	return re.compile('"id":(\d+),.+?"md5":"(.+?)",.+?"file_ext":"(png|jpg)","file_url":"(.+?)",.+?"sample_url":"(.+?)",').findall(html)
	"""在源码里用正则表达式匹配图的下载地址  
0=id 1=MD5 2=格式 3=PNG的URL(格式是JPG时URL则是JPG的URL) 4=JPG的URL

	<a class="directlink .+?img" href="(.+?)">
	"(sample|file)_url":"(.+?)",
"id":(\d+),.+?"file_ext":"png","file_url":"(.+?)",.+?"sample_url":"(.+?)",
"id":(\d+),.+?"md5":"(.+?)",.+?"file_ext":"(png|jpg)","file_url":"(.+?)",.+?"sample_url":"(.+?)",
	"""


def get_htmltags(tags,page=1):
	url_tags='https://yande.re/post?page='+str(page)+'&tags='+tags
	html_tags=Http.get_Source(url_tags).decode('utf-8')
	return html_tags
#print(get_list(get_htmltags(tags)))
#tags='masa_(mirage77)'
star=1
def get_lastpage(html_tags:str):
#	if not re.findall(html_tags):
#		re.findall(html_tags)[0]=str(star)
#	else:
	return re.compile('(\d+)</a> <a class="next_page"').findall(html_tags)

"""
def get_Oldpngfilename(file_path:str):
	return re.compile('re%20(\d+)%20.+?.png').findall(file_path)

def get_Oldjpgfilename(file_path:str):
	return re.compile('re%20(\d+)%20.+?.jpg').findall(file_path)
"""
#print(get_Oldjpgfilename(Log.create_tagslog('izumi_tsubasu')))



#def get_md5(file_name):
#	md5=hashlib.md5(open(file_name,'rb').read()).hexdigest()
#	return md5
#print (Function.tags_folder(tags))

#print(get_lastpage(get_htmltags(tags,1)))
#page=2
#tags='izumi_tsubasu'
#print(get_list(get_htmltags(page,tags)))