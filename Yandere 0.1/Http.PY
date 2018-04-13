import urllib.request

def get_Source(url: str, header: list = {}):
	header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
	header['Accept-Language'] = 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7'
	header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
	req = urllib.request.Request(url, headers=header)
	return urllib.request.urlopen(req).read()#.decode('utf-8')