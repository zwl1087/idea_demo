import pytest
from selenium.webdriver.common.by import By
from time import sleep


class TestWindows():

    def test_window(self,open_browser):
        dr = open_browser
        dr.get("https://www.baidu.com")
        dr.maximize_window()
        dr.find_element(By.CSS_SELECTOR,"#s-top-loginbtn").click()
        sleep(2)
        dr.find_element(By.CSS_SELECTOR,"#TANGRAM__PSP_11__regLink").click()

        # 当前窗口的句柄
        print(dr.current_window_handle)
        # 所有窗口的句柄
        print(dr.window_handles)

        windows = dr.window_handles
        # 通过窗口句柄，切换窗口
        dr.switch_to.window(windows[-1])

        # 在新窗口进行操作
        dr.find_element(By.ID,"TANGRAM__PSP_4__userName").send_keys("zwl@xnf")
        dr.find_element(By.ID,"TANGRAM__PSP_4__phone").send_keys("zwl@xnf")

        # 通过窗口句柄，切换窗口：返回原窗口
        dr.switch_to.window(windows[0])

        # 在原窗口进行操作
        dr.find_element(By.ID,'TANGRAM__PSP_11__userName').send_keys("18534966361")
        dr.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys("405181087.0a")
        # dr.find_element(By.ID,"TANGRAM__PSP_11__submit").click()
        sleep(3)


        for code in [1,2,3,4,5,6]: print(code)



