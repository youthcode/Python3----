from requests import Request, Session

url = 'https://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)




# import requests

# proxies = {
#     'http': 'socks5h://127.0.0.1:1082',
#     'https': 'socks5h://127.0.0.1:1082',
# }

# response = requests.get('https://httpbin.org/ip', proxies=proxies)
# # response = requests.get('https://ipinfo.io/json', proxies=proxies)
# responseOri = requests.get('https://httpbin.org/ip')


# print(response.json())
# print(responseOri.json())





# import requests
# from requests_oauthlib import OAuth1

# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)





# import requests

# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)





# import requests
# from requests.auth import HTTPBasicAuth

# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# print(r.status_code)





# import requests

# r = requests.get('https://httpbin.org/get', timeout=1)
# print(r.status_code)





# import requests

# response = requests.get('https://ssr2.scrape.center/')
# print(response.status_code)





# import requests

# s = requests.Session()
# s.get('https://httpbin.org/cookies/set/number/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)





# import requests

# requests.get('https://httpbin.org/cookies/set/number/123456789')
# r = requests.get('https://httpbin.org/cookies')
# print(r.text)





# import requests

# cookies = '_octo=GH1.1.581055246.1717056553; _device_id=2f4aeb26d612e1f270ec19fab234a782; saved_user_sessions=2271853%3AOCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; user_session=OCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; __Host-user_session_same_site=OCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; logged_in=yes; dotcom_user=youthcode; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=D08RoI9ZFnbTTqPXzIHm5YbMoJM8QaM6YHxjZGF%2Fa%2B8kojALwW2nDNbb0dh0rWh0rvO0ilcU%2Bb6hkYOYp2GNpxbonjT626eXq6e%2BsBGXhbgE9IBTqYE8AvRfGam3STtHKTRfzWEhlsTYAUZ%2FYbDBrL8qfL7%2BHfaqk%2FiI%2Fr4GU5sv%2BegKfrXY4x7YM3hBQ2kD8mKTSvztu9D4y1pRwJ7gAlBxgdPnXstiRTk%2F1%2BPr4C%2Fy0YZWE7eD05vVDWOaN8q3Ucm0Y8hv6CzWEeB7Iry%2F%2FZjOEnQO%2FoRoJ5ik4iOVh5eHjYvPWu5BhNJ0xwS5po%2BWdaHxaK%2F%2FwQQ2EUR0H%2BE1eF2F2hYtHJXpO61XbTg7WY034ANyfoxz3HEIfcaDRPK%2F--GpmtVGfZZ0xeqhR7--LVwEs8Nyww8yvscxAJS25w%3D%3D'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36'
# }
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get('https://github.com/', cookies=jar, headers=headers)
# print(r.text)





# import requests

# headers = {
#     'Cookie': '_octo=GH1.1.581055246.1717056553; _device_id=2f4aeb26d612e1f270ec19fab234a782; saved_user_sessions=2271853%3AOCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; user_session=OCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; __Host-user_session_same_site=OCtiGPL-5Z260lmA5q6nCkYfbyjZXepy7clnM0InHrOjsUUQ; logged_in=yes; dotcom_user=youthcode; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=D08RoI9ZFnbTTqPXzIHm5YbMoJM8QaM6YHxjZGF%2Fa%2B8kojALwW2nDNbb0dh0rWh0rvO0ilcU%2Bb6hkYOYp2GNpxbonjT626eXq6e%2BsBGXhbgE9IBTqYE8AvRfGam3STtHKTRfzWEhlsTYAUZ%2FYbDBrL8qfL7%2BHfaqk%2FiI%2Fr4GU5sv%2BegKfrXY4x7YM3hBQ2kD8mKTSvztu9D4y1pRwJ7gAlBxgdPnXstiRTk%2F1%2BPr4C%2Fy0YZWE7eD05vVDWOaN8q3Ucm0Y8hv6CzWEeB7Iry%2F%2FZjOEnQO%2FoRoJ5ik4iOVh5eHjYvPWu5BhNJ0xwS5po%2BWdaHxaK%2F%2FwQQ2EUR0H%2BE1eF2F2hYtHJXpO61XbTg7WY034ANyfoxz3HEIfcaDRPK%2F--GpmtVGfZZ0xeqhR7--LVwEs8Nyww8yvscxAJS25w%3D%3D',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36'
# }
# r = requests.get('https://github.com', headers=headers)
# print(r.text)





# import requests

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)





# import requests

# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)





# import requests

# r = requests.get('https://ssr1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)





# import requests

# data = {'name': 'germey', 'age': '25'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)





# import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36'
# }
# r = requests.get('https://ssr1.scrape.center/', headers=headers)
# print(r.text)
    





# import requests

# r = requests.get('https://scrape.center/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)





# import requests

# r = requests.get('https://scrape.center/favicon.ico')
# print(r.text)
# print(r.content)





# import requests
# import re

# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)





# import requests

# r = requests.get('https://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))





# import requests

# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)





# import requests

# r = requests.get('http://httpbin.org/get')
# print(r.text)





# import requests

# r = requests.get('http://httpbin.org/get')
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.patch('http://httpbin.org/patch')





# import requests

# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:100])
# print(r.cookies)