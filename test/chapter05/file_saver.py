import requests
from pyquery import PyQuery as pq
url = 'https://www.zhihu.com/explore'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
response = requests.get(url, headers=headers)
html = response.text
doc = pq(html)
items = doc('.ExploreSpecialCard-contentList .ExploreSpecialCard-contentItem').items()
for item in items:
    tag = item.find('.ExploreSpecialCard-contentTag').text()
    title = item.find('.ExploreSpecialCard-contentTitle').text()
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([tag, title]))
        file.write('\n' + '=' * 100 + '\n')
