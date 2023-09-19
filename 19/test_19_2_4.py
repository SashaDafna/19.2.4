import pytest
from app.calculator import Calculator


# тестим Calculator через набор позитивных тестов
class TestCalc:
    def setup(self):
        self.calc = Calculator
        print('Метод setup')

    def test_multiply_success(self):
        assert self.calc.multiply(self, 11, 2) == 22
        print('Выполнение умножения')

    def test_division_success(self):
        assert self.calc.division(self, 11, 2) == 5.5
        print('Выполнение деления')

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 11, 0)
            print('Выполнение деления на ноль выдаёт положенную ошибку')

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 11, 2) == 9
        print('Выполнение вычитания')

    def test_adding_success(self):
        assert self.calc.adding(self, 11, 2) == 13
        print('Выполнение сложения')

    def teardown(self):
        print('Метод teardown')
