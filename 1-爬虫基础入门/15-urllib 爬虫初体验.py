from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('BaiduSpider', 'https://www.baidu.com'))
print(rp.can_fetch('BaiduSpider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))






# from urllib.parse import unquote

# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))





# from urllib.parse import quote

# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)





# from urllib.parse import parse_qsl

# query = 'name=germey&age=25'
# print(parse_qsl(query))





# from urllib.parse import parse_qs

# query = 'name=germey&age=25'
# print(parse_qs(query))





# from urllib.parse import urlencode

# params = {
#     'name': 'germey',
#     'age': 25
# }
# base_rul = 'http://www.baidu.com?'
# url = base_rul + urlencode(params)
# print(url)





# from urllib.parse import urljoin

# print(urljoin('https://www.baidu.com', 'FAQ.html'))
# print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# print(urljoin('https://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))





# from urllib.parse import urlunsplit

# data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))





# from urllib.parse import urlsplit

# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result.scheme, result[0])





# from urllib.parse import urlsplit

# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result)





# from urllib.parse import urlunparse

# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))





# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
# print(result.scheme, result[0], result.netloc, result[1], sep='\n')





# from urllib.parse import urlparse

# result = urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
# print(result)





# from urllib.parse import urlparse

# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)




# from urllib.parse import urlparse

# result = urlparse('http://wwww.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)





# from urllib.parse import urlparse

# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result))
# print(result)





# import socket
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')





# from urllib import request, error

# try:
#     response = request.urlopen('http://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')





# from urllib import request, error

# try:
#     response = request.urlopen('http://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')





# from urllib import request, error

# try:
#     response = request.urlopen('http://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason)





# import urllib.request, http.cookiejar

# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))