import requests
from urllib import request
import socks
import socket
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = 'mensyli4:Xy1234!@#@127.0.0.0:7453'
proxy_handler = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e)


socks.setdefaultproxy(socks.SOCKS5, '127.0.0.1', '7453')
socket.socket = socks.socksocket
try:

    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e)


proxy = '127.0.0.1:7742'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(e)
