import pytest
import allure

@allure.feature("登录模块")
class TestLoginMoudel():
    @allure.story("登录成功")
    @allure.title("Login_No.001_登录成功")
    def test_login_success(self):
        print("登录成功")

    @allure.story("登录成功")
    @allure.title("Login_No.002_登录成功")
    def test_login_success(self):
        print("登录成功测试失败")
        assert False

    @allure.story("登录失败")
    @allure.title("Login_No.003_登录失败")
    def test_login_fail(self):
        print("登录失败")

    @allure.story("登录失败")
    @allure.title("Login_No.004_登录失败")
    @pytest.mark.skip()
    def test_login_fail(self):
        print("登录失败, 不执行这个用例")

@allure.feature("搜索模块")
class TestSearchModel():
    @allure.story("搜索成功")
    @allure.title("Search_NO.001_搜索成功")
    def test_search_success(self):
        print("search success")

    @allure.story("搜索失败")
    @allure.title("Search_NO.002_搜索失败")
    def test_search_fail(self):
        print("search fail")

    @allure.story("搜索失败")
    @allure.title("Search_NO.003_搜索失败")
    def test_search_fail(self):
        print("search fail")
        raise Exception ("oops")



# # 使用fixture
# def test_fixture_demo(open_browser):
#     print("we are testing fixture now")
#
# def test_fixture_demo_1(open_browser,connet_db):
#     print("we are testing fixture now")
