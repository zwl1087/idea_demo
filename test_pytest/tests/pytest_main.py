import pytest

'''
1、使用 pytest.main() 执行测试用例，测试使用的解释器是python解释器，而不是pytest
2、执行方式：【命令行】python pytest_main.py
3、在main() 添加命令，用一个列表来传参，参数内容为pytest 命令行的参数
'''



if __name__ == '__main__':
    # 1、运行当前目录下的所有测试用例
    pytest.main()
    # 2、运行模块中的某一条测试用例
    pytest.main(["test_pytest_frame.py::test_case_2","-vs"])
    # 3、运行某个标签的测试用
    pytest.main(["test_pytest_frame.py", "-vs","-m","webtest"])


