import urllib.request
import requests
import re
import os
import http.cookiejar
#import urllib.parse
_folder_name ='E:/Danbooru/'
if not os.path.exists(_folder_name):
	os.makedirs(_folder_name)

posts=2800000
max_poste=2800020
while posts<=max_poste:
	s='http://danbooru.donmai.us'
	url='https://danbooru.donmai.us/posts/'+str(posts)
	"""
	header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
	header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2883.103 Safari/537.36'
	'accept-encoding': 'gzip, deflate, br'
	"""
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Language' : 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7'}
	req = urllib.request.Request(url,headers=headers)
	code=requests.get(url).status_code
	print(code)
	if code!=200:
		posts=posts+1
		continue
	else:
#		urllib.request.urlopen(req).read().decode
		dlurl=re.compile('Size: <a href="(.*?)">')
		info=dlurl.findall(urllib.request.urlopen(req).read().decode('utf-8'))
		posts=posts+1
#		imgurl=dlurl.findall(urllib.request.urlopen(req).read().decode('utf-8'))
		if not info:
			continue
		else:
			file_name=info[0].split('/')[-1]
			print(info)
			print(file_name)	
			if 'https://' in info[0]:
				for x in info:
					urllib.request.urlretrieve(info[0],_folder_name+'/'+str(posts)+file_name)
			else:
				print('http://danbooru.donmai.us'+info[0])
				for x in info:
					urllib.request.urlretrieve('http://danbooru.donmai.us'+info[0],_folder_name+'/'+str(posts)+file_name)
