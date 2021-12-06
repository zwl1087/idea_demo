import pytest

'''
python 异常处理 try except
pytest 异常处理 pytest.pytest.raises()
'''

def data_sub(a,b):
    try:
        c = a / b
        print("您输入的数字计算结果为：",c)
        return c
    except (ValueError,ArithmeticError) as e:
        raise Exception("程序发生了数字格式异常，算数异常之一")
        return None
    except:
        print("未知异常")

    print("程序继续运行")

@pytest.mark.parametrize("a,b,c",[(10,2,5.0),(5,"ccc",None)])
def test_data_int(a,b,c):
    # print(data_sub(a,b))
    assert c == data_sub(a,b)

def test_py_raise():
    # 可以捕获特定的异常
    with pytest.raises(ValueError,match="must be 0 or None"):
        raise ValueError("value must be 0 or None")

def test_py_raise_info():
    # 获取捕获的异常细节
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"



