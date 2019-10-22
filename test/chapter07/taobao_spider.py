import pymongo
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = '小米9'


def login():
    print('start login....')
    url = 'https://login.taobao.com/member/login.jhtml'
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)
    browser.find_element_by_id('J_Quick2Static').click()
    username = browser.find_element_by_id('TPL_username_1')
    username.send_keys('user')
    time.sleep(3)
    password = browser.find_element_by_id('TPL_password_1')
    password.send_keys("passwd")
    time.sleep(1)
    dragger = browser.find_element_by_id('nc_1_n1z')
    action = ActionChains(browser)
    for index in range(500):
        try:
            action.drag_and_drop_by_offset(dragger, 500, 0).perform()
        except Exception:
            break
    print('*')
    browser.find_element_by_id('J_SubmitStatic').click()
    print('@')


def parse_page(page):
    print('正在爬取{}页'.format(str(page)))
    try:
        url = 'https://s.taobao.com/search?q={}'.format(quote(KEYWORD))
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
            time.sleep(5)
            print(browser.current_url)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_shopping()
    except TimeoutException as e:
        print(e)
        parse_page(page)
    except Exception as e:
        print(e)


def get_shopping():
    html_source = browser.page_source
    doc = pq(html_source)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        good = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(good)
        save_to_mongo(good)


MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTIONS = 'goods'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTIONS].insert_one(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


MAX_PAGE = 5


def main():
    login()
    for page in range(1, MAX_PAGE + 1):
        parse_page(page)


if __name__ == '__main__':
    main()
