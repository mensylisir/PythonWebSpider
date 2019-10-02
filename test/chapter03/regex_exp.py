import re

content1 = '2019-10-01 12:00:30'
content2 = '2019-10-11 22:34:56'
content3 = '2019-11-02 08:56:01'
pattern = re.compile('\d{2}:\d{2}', re.S)
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1)
print(result2)
print(result3)
