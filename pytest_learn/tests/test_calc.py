import pytest

from pytest_learn.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    # 正常值例子
    # 整数
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [4, -1, -4]
    ])
    def test_mul_int(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 浮点数
    @pytest.mark.parametrize('a, b, c', [
        [0.3, 0.2, 0.06],
        [-0.4, -0.2, 0.08],
        [0.3, -0.7, -0.21],
        [0.1, 0.1, 0.01]
    ])
    def test_mul_float(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 整数浮点数混合
    @pytest.mark.parametrize('a, b, c', [
        [1, -0.2, -0.2],
        [0.3, -4, -1.2],
        [0.2, 5, 1]
    ])
    def test_mul_mix(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @pytest.mark.parametrize('a, b', [
        ['a', 's'],
        ['d', 'v'],
    ])
    def test_mul_Type(self, a, b):
        with pytest.raises(TypeError):
            assert self.calc.div(a, b)

    # 正常值例子
    # 整数
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [3, -3, -1],
        [0, 2, 0],
        [-6, -3, 2],
        [-6, 2, -3]
    ])
    def test_div_int(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 浮点数
    @pytest.mark.parametrize('a, b, c', [
        [0.02, 0.2, 0.2],
        [0.06, -0.3, -0.2],
        [0, 0.2, 0],
        [-0.08, 0.2, -0.4],
        [-0.12, -0.4, 0.3]
    ])
    def test_div_float(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 整数和浮点数
    @pytest.mark.parametrize('a, b, c', [
        [2, 0.2, 10],
        [0.4, -2, -0.2],
        [0.4, -0.2, -2],
        [0.6, 0.3, 2],
        [-0.08, 0.02, -4],
        [-0.12, -0.04, 3]
    ])
    def test_div_mix(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div_Zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)

    @pytest.mark.parametrize('a, b', [
        ['a', 's'],
        ['d', 'v'],
    ])
    def test_div_Type(self, a, b):
        with pytest.raises(TypeError):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process1(self):
        r1=self.calc.mul(1, 2)
        r2=self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2

    def test_process2(self):
        r1=self.calc.div(1, 2)
        r2=self.calc.mul(2, 1)
        assert r1 == 0.5
        assert r2 == 2

if __name__ == '__main__':
    pytest.main(['test_calc.py', '-v'])