import urllib.request

url = 'https://www.baidu.com'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_read = response.read()
print(request, '\n', response, '\n', data_read)

