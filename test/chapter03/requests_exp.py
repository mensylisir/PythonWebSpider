import requests

cookie_text = '_zap=a56cfd45-55ce-4b1e-b99c-4f4636cd0cd2; _xsrf=Kjtl4nkLdwZv139IZg0ID8pNemGz7uWh; d_c0="AEAj63ICBxCPTou4Y-qHT9MgPAnKT17u7fs=|1568128310"; q_c1=cb61b550afd94fa3bf76dcca0bad6862|1568128344000|1568128344000; __utmv=51854390.000--|3=entry_date=20190910=1; l_cap_id="ZTEyMjkxNGE2MGY3NDk2YTkwZmQ2MmVjZGQ1ZWEwZjI=|1568563030|66ac9678300870aa6e83180c5250aee899cb7a08"; r_cap_id="YmFhOWVkMWM1ODQyNDBmMWEyMGE4MjRhZDcwMGY4YWE=|1568563030|7f0b564fd0fdbf0ba14b9e8adb8c10422f83483b"; cap_id="YzY0ZWU4Zjk5MDEzNDJhYWIzN2Q1YTZmNmM0MWMwZGY=|1568563030|8a01db841c3b81ff6854d3c08e6369e1f7a4c253"; __utma=51854390.1229907438.1568128343.1568128343.1568563035.2; __utmz=51854390.1568563035.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569856046,1569922607,1569987852,1569997473; capsion_ticket="2|1:0|10:1570002915|14:capsion_ticket|44:ZmViMzg3YzVkOGJjNDdhZmE2ZmExMWNjNzg3NmI5MzQ=|46cb42cee6a855485104127345aa1e85f665351b3c9913ea7d12804084ab4f79"; z_c0="2|1:0|10:1570002953|4:z_c0|92:Mi4xRGJMeURBQUFBQUFBUUNQcmNnSUhFQ2NBQUFDRUFsVk5DZVc3WFFCMnpHQ21BMk1MaXEyUWpTQjVCVExIekM4cUNR|34e193193db12bc56a057369a6cba57629f071426abf09ae95362b807f92ee2c"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1570002954'
cookies = {}
for item in cookie_text.split('; '):
    key, value = item.split('=', 1)
    cookies[key] = value

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Host': 'www.zhihu.com',
}
response = requests.post('https://www.zhihu.com/', cookies=cookies, headers=headers)
print(response.text)
