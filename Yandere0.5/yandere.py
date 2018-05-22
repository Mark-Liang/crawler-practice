import re
import Http
 

def get_html(page=1):
	url='https://yande.re/post?page='+str(page)
	html=Http.get_Source(url).decode('utf-8')
	return html

def get_list(html:str):
	return re.compile('"id":(\d+),.+?"md5":"(.+?)",.+?"file_ext":"(png|jpg)","file_url":"(.+?)",.+?"sample_url":"(.+?)",').findall(html)
	"""在源码里用正则表达式匹配图的下载地址  
0=id 1=MD5 2=格式 3=PNG的URL(格式是JPG时URL则是JPG的URL) 4=JPG的URL
"""

def get_htmltags(tags,page=1):
	url_tags='https://yande.re/post?page='+str(page)+'&tags='+tags
	html_tags=Http.get_Source(url_tags).decode('utf-8')
	return html_tags

def get_lastpage(html_tags:str):
	return re.compile('(\d+)</a> <a class="next_page"').findall(html_tags)
