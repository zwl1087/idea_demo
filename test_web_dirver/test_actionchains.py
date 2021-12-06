#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/11/20

"""

from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWebdriverActions(object):
    def setup_class(self):
        option = Options()
        # 修改示例属性为 debug 模式的 ip+port
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options = option)

        # 隐式等待，这是全局等待时间
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.close()

    @pytest.mark.skip
    def test_actions(self):
        try:
            self.driver.get("https://mail.qq.com/cgi-bin/loginpage")

            iframe = self.driver.find_element(By.ID, "login_frame")
            self.driver.switch_to.frame(iframe)

            self.driver.find_element(By.ID, "u").send_keys("405181087@qq.com")
            self.driver.find_element(By.ID, "p").send_keys("car123bus.0")

            sleep(15)

            # print(" iframe 已经切换了 ")
            #
            # # self.driver.find_element(By.ID,"qqLoginTab").click()
            # self.driver.find_element(By.ID,"u").send_keys("405181087@qq.com")
            # self.driver.find_element(By.ID,"p").send_keys("car123bus.0")
            # print(" 信息输入成功了")
            # self.driver.find_element(By.ID,"login_button").click()
            #
            cookies_qq_mail = self.driver.get_cookies()
            with open("cookies_qqmail.yaml", "w") as f:
                yaml.safe_dump(cookies_qq_mail, f)

            # print(" 登录请求已发送了")

            # mainFrame
            sleep(2)
        except Exception as e:
            print(e)

    @pytest.mark.skip
    def test_login_by_cookies(self):
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")
        cookies = yaml.safe_load(open("cookies_qqmail.yaml"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://mail.qq.com/cgi-bin/loginpage")
        self.driver.refresh()

    # @pytest.mark.skip
    def test_action_chains_scroll(self):
        self.driver.get("https://blog.csdn.net/")

        # 显示等待： 自定义函数必须给一个参数x: 因为 until() 函数调用wait时候会将driver 传递给x
        def wait(x):
            re_list = self.driver.find_elements(By.CSS_SELECTOR, '.toolbar-btn')
            print(len(re_list))
            return len(re_list) >= 1

        # 显示等该： 只作用于该步骤，如果该步骤执行完成，则不再等待
        WebDriverWait(self.driver, 3).until(wait)
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-report-query="spm=3001.4506"]').click()
        # 显示等待的第二种用法，使用 expected_conditions 函数：
        # 【注意】：expected_conditions。presence_of_element_located() 参数是一个元组(By.CSS_SELECTOR,'.login-box-tabs-items span:nth-child(2)')
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.login-box-tabs-items span:nth-child(2)')))
        # 选择账号密码登录
        self.driver.find_element(By.CSS_SELECTOR, '.login-box-tabs-items span:nth-child(2)').click()
        # 输入账号密码并点击登录
        self.driver.find_element(By.CSS_SELECTOR, '.base-input-text[type="text"]').send_keys('18534966361')
        self.driver.find_element(By.CSS_SELECTOR, '.base-input-text[type="password"]').send_keys('405181087.0a')
        self.driver.find_element(By.CSS_SELECTOR, '.base-button').click()
        # 等待滑块可以滑动
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="nc_iconfont btn_slide"]')))
        # 添加滑动滑块事件
        action = ActionChains(self.driver)
        # 定位被滑动的元素
        element = self.driver.find_element(By.CSS_SELECTOR, 'span[class="nc_iconfont btn_slide"]')
        # 按照水平、垂直位移滑动滑块： 横坐标设置较大值，纵坐标设施为 0
        action.drag_and_drop_by_offset(element, 300, 0)
        # 执行 Action 事件
        action.perform()
        print(" 登录滑块已经滑动了 ")

    @pytest.mark.skip
    def test_action_chains_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")

        action = ActionChains(self.driver)
        element_clik = self.driver.find_element(By.CSS_SELECTOR, 'input[value="click me"]')
        element_double_clik = self.driver.find_element(By.CSS_SELECTOR, 'input[value="dbl click me"]')
        element_right_clik = self.driver.find_element(By.CSS_SELECTOR, 'input[value="right click me"]')

        action.click(element_clik)
        action.double_click(element_double_clik)
        action.context_click(element_right_clik)

        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_action_chains_moveto(self):
        self.driver.get("https://www.baidu.com/")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "s-usersetting-top")))
        element_moveto = self.driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(element_moveto)
        action.perform()
        sleep(3)

    def test_action_chains_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_darg = self.driver.find_element(By.ID, "dragger")
        element_drop = self.driver.find_element(By.XPATH, '//*[@class="item"][1]')
        action = ActionChains(self.driver)
        action.drag_and_drop(element_darg, element_drop).pause(2)
        action.perform()

    def test_action_chains_send_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("uesrname").pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACKSPACE).pause(2)
        action.perform()


TODO = "tianjia"
