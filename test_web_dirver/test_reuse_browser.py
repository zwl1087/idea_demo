from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
# 修改示例属性为 debug 模式的 ip+port
option.debugger_address = "localhost:9222"
# 实例化webdriver 时添加 opention 参数
driver = webdriver.Chrome(options = option)

driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
sleep(10)


