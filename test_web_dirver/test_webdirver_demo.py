from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestHogwarts:
    def setup(self):
        self.dirver = webdriver.Chrome()
        self.dirver.get("https://www.baidu.com/")
        # 设置隐式等待
        self.dirver.implicitly_wait(5)

    def teardown(self):
        self.dirver.quit()
        pass

    def test_baidu_search(self):
        self.dirver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        # sleep(1)
        self.dirver.find_element(By.ID,"su").click()
        # sleep(1)
        self.dirver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页")



