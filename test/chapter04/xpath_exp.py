from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/ancestor::*')
result = html.xpath('//li[1]/ancestor::div')
result = html.xpath('//li[1]/attribute::*')
result = html.xpath('//li[1]/child::*')
result = html.xpath('//li[1]/child::a[@href="link1.html"]/text()')
result = html.xpath('//ul/descendant::*')
result = html.xpath('//li[1]/descendant::span/text()')
result = html.xpath('//li[1]/following::*')
result = html.xpath('//li[1]/following::*[2]')
result = html.xpath('//li[1]/following-sibling::*')
print(result)
