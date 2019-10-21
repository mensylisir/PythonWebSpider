from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

browser = webdriver.Chrome()
try:
    browser.get('https://www.zhihu.com/explore')
except TimeoutException:
    print('Timeout')
try:
    browser.find_element_by_id('hehe')
except NoSuchElementException:
    print('No such element')
finally:
    browser.close()
