
class TestDemo():
    def test_first_demo(self):
        a = 1
        try:
            a += 1
        except :
            a += 2
        else:
            a += 1
        finally:
            a += 1
        assert a == 4
    def test_second_demo(self):
        a = 1
        b = 2
        assert a+b == 3

class TestAnotherDemo():
    def test_demo_1(self):
        a = 1
        assert a < 3

    def test_demo_2(self):
        a = 1
        assert a > 3
