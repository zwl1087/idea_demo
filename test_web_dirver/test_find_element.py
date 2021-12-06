from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFindElement():
    def setup(self):
        self.drievr = webdriver.Chrome()
        self.drievr.get("https://www.baidu.com/")
        self.drievr.implicitly_wait(1)

    def teardown(self):
        self.drievr.quit()

    def test_find_element_by_id(self):
        self.drievr.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.drievr.find_element(By.CSS_SELECTOR, '#su').click()
        sleep(3)
        req_name = self.drievr.find_elements(By.XPATH, '//*[@id="content_left"]//h3/a')
        req_name_list = []
        for req in req_name:
            req_name_list.append(req)
            print(req.text)
        # assert '霍格沃兹测试学院 - 主页' in req_name
