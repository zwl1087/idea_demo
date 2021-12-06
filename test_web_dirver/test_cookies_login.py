from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookiesLogin():
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def teardown_class(self):
        self.driver.close()

    # @pytest.mark.skip

    # 【登录后获取cookies,并保存】
    def test_get_cookies(self):
        # 进入登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 设置超长登录时间，在浏览器手动做登录操作
        sleep(15)
        # 获取cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        # 将cookies文件添加至本地yaml配置文件
        with open("../data/cookies.yaml", "w") as f:
            yaml.safe_dump(cookies, f)

    # 【 用cookies登录页面 】
    @pytest.mark.skip
    def test_cookies_login(self):
        # 1、 打开登录的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 2、打开保存cookies的文件
        cookies = yaml.safe_load(open("cookies.yaml"))
        for cookie in cookies:
            # 3、 添加cookies
            self.driver.add_cookie(cookie)
        sleep(3)
        # 4、添加cookies后重新登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 5、验证登录成功
        sleep(5)
