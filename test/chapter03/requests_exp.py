from requests import Request, Session

url = "http://httpbin.org/post"
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

session = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = session.prepare_request(req)
response = session.send(prepped)
print(response.text)
