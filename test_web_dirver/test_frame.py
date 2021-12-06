import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class TestFrame():
    def setup_class(self):
        option = Options()
        # 修改示例属性为 debug 模式的 ip+port
        option.debugger_address = "localhost:9222"
        # 实例化webdriver 时添加 option 参数
        driver = webdriver.Chrome(options = option)

        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(10)

    def test_frame(self):
        pass
