from bs4 import BeautifulSoup
import re

html = '''
    <html>
        <head>
            <title>Demo</title>
        </head>
        <body>
            <div>
                <ul class="hhh">
                    <a href="link1.html">first1 item</a>
                    <a href="link111.html">first2 item</a>
                    <li class="item1 item10" id="li1"><a href="link1.html">first3 item</a>
                    <a href="link111.html">first4 item</a>
                    <span>8888888</span></li>
                    <li class="item2" name="item2" id="li2"><a href="link2.html">second item</a>
                    <li class="item2" id="li3"><a href="link3.html">third item</a></li>
                    <li class="item4" id="li4"><a href="link4.html">fourth item</a></li>
                    <li class="item5" id="l54"><a href="link5.html">fivth item</a></li>
                    <li class="item6" id="li6"><a href="link6.html">sixth item</a></li>
                </ul>
            </div>
        </body>
    </html>
'''
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    for li in ul.select('li'):
        for a in li.select('a'):
            print(a.get_text())
