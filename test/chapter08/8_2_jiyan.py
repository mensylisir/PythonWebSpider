from selenium import webdriver
import time
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
EMAIl = '1111111'
PASSWORD = '1111111'
BORDER = 6


class CrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
        self.email = EMAIl
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def get_geetest_button(self):
        button = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_postion(self):
        image = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'geetest_canvas_img ')))
        time.sleep(2)
        location = image.location
        size = image.size
        top, bottom, left, right = location['y'], location['y'] + \
            size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    def get_geetest_image(self, name='captcha.png'):
        top, bottom, left, right = self.get_postion()
        print('验证码位置:', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((top, bottom, left, right))
        captcha.save(name)
        return captcha

    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def is_pixel_equal(self, image1, image2, x, y):
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold \
                and pixel1[1] - pixel2[1] < threshold \
        and pixel1[2] - pixel2[2] < threshold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        track = []
        current = 0
        mid = distance * 4 / 5
        t = 0.2
        v = 0

        while current < distance:
            if current < mid:
                a = 2

            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1/2 * a * t * t
            current += move
            track.append(round(move))
        return track

    def move_to_gap(self, slider, track):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(
                xoffset=x, yoffset=0).perform()
        time.sleep(1)
        ActionChains(self.browser).release().perform()

    def open(self):
        self.browser.maximize_window()
        self.browser.get(self.url)
        input = self.browser.find_elements_by_css_selector(
            'div.ivu-form-item-content input.ivu-input')
        email = input[0]
        password = input[1]
        time.sleep(2)
        email.send_keys(self.email)
        time.sleep(2)
        password.send_keys(self.password)
        time.sleep(2)

    def login(self):
        submit = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def crack(self):
        self.open()
        button = self.get_geetest_button()
        button.click()
        image1 = self.get_geetest_image('captcha1.png')
        slider = self.get_slider()
        slider.click()
        image2 = self.get_geetest_image('captcha2.png')
        gap = self.get_gap(image1, image2)
        print('缺口位置', gap)
        gap -= BORDER
        track = self.get_track(gap)
        print('滑动轨迹', track)
        self.move_to_gap(slider, track)

        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        print(success)

        # 失败后重试
        if not success:
            self.crack()
        else:
            self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
