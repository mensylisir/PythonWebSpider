
html = '''
    <div>
        <ul>
        <li class="item1 item10">
            <a href="link1.html">first item</a>
            <a href="link111.html" class="a2">first11 item</a>
        </li>
        <li class="item2" name="item2">
            <a href="link2.html">second item</a>
        </li>
        <li class="item2">
            <a href="link3.html">third item</a>
        </li>
        <li class="item4">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item5" id="li5">
            <a href="link5.html">fivth item</a>
        </li>
        <li class="item6">
            <a href="link6.html">sixth item</a>
        </li>
        </ul>
    </div>
'''

from pyquery import PyQuery as pq
import requests
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(sixth)')
print(li)
