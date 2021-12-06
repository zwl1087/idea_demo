import pytest
import sys

# 模块级别 执行模块的前后分别执行 setup_module teardown_module
def setup_module():
    print("资源准备：setup_module")
def teardown_module():
    print("资源准备：teardown_module")

# 模块方法级 测试用例，定义在模块中
def test_case_1():
    print("test_case_1")
def test_case_2():
    print("test_case_2")

# 执行方法的前后分别执行 setup_function teardown_function
def setup_function():
    print("资源准备：setup_function")
def teardown_function():
    print("资源准备：teardown_function")


class TestDemo1:
    # 执行类 前后分别执行 setup_class teardown_class 仅执行一次
    def setup_class(self):
        print(" TestDemo1 setup_class")
    def teardown_class(self):
        print(" TestDemo1 teardown_class")

    @pytest.mark.webtest
    def test_case_3(self):
        print("test_case_3:  @pytest.mark.webtest ")

    @pytest.mark.webtest
    def test_case_4(self):
        print("test_case_4:  @pytest.mark.webtest ")

    @pytest.mark.apptest
    def test_case_5(self):
        print("test_case_5:  @pytest.mark.apptest")

    @pytest.mark.apptest
    def test_case_6(self):
        print("test_case_6:  @pytest.mark.apptest")


    # 每个类的方法前后分别执行：setup teardown
    def setup(self):
        print("TestDemo1 setup")
    def teardown(self):
        print("TestDemo1 teardown")
    # 每个类的方法前后分别执行：setup_method teardown_method
    def setup_method(self):
        print(" TestDemo1 setup_method")
    def teardown_method(self):
        print(" TestDemo1 teardown_method")

    # skip标签使用，跳过该用例执行
    @pytest.mark.skip(reason="跳过这个测试用例")
    def test_case_7(self):
        print("test_case_7")
    # 有添加判断的跳过
    @pytest.mark.skipif(reason="我还没开发完成，我不执行")
    def test_case_8(self):
        print("test_case_8")

    # 在代码中使用 skip,执行到pytest.skip()时,跳过后面的用例，此时测试用例标记为跳过
    def test_case_9(self):
        print("test_case_9")
        if 1 < 2:
            pytest.skip(" 条件不满足，我跳过执行了 ")
        print(" 跳过条件不满足，我可以执行了 ")


    # @pytest.mark.skipif： 如果满足skipif 里的条件，才回去执行测试用例，否则不执行

    @pytest.mark.skipif(sys.platform == 'win',reason= " windows 系统不执行这个用例")
    def test_case_10(self):
        assert True
    @pytest.mark.skipif(sys.platform == 'darwin',reason= " mac 系统不执行这个用例")
    def test_case_11(self):
        assert True

    @pytest.mark.skipif(sys.version_info < (4,6),reason= " python 版本太低，不执行这个用例")
    def test_case_12(self):
        assert True

    @pytest.mark.xfail
    def test_case_13(self):
        # 测试过程仍然会被执行
        print(" 我是test_case_13 的测试过程 ")
        # 如果断言通过，执行结果会标记为 XPASS
        assert True

    @pytest.mark.xfail
    def test_case_14(self):
        print(" 我是test_case_14 的测试过程 ")
        # 如果断言通过，执行结果会标记为 XFAIL
        assert False

    xfail = pytest.mark.xfail

    @xfail(reason="这是一个BUG, BUG001")
    def test_case_15(self):
        assert False
    # 代码里调用 xfail
    def test_case_16(self):
        print(" 开始测试 xfail ")
        pytest.xfail(reason="功能未完成，这个用例不执行")
        #  pytest.xfail() 后面的部分不执行了： 不执行测试过程
        print("这是测试过程")
        assert 1==1



