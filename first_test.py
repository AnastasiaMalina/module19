import pytest
from app.calculator import Calculator



class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):    # test "*"
        assert self.calc.multiply(self, 2, 2) == 4    # 2 * 2 = 4

    def test_multiply_calculation_failed(self):    # fail_test "*"
        assert self.calc.multiply(self, 2, 2) == 5  # 2 * 2 != 5

    def test_substraction_calculate_correctly(self): # test "-"
        assert self.calc.subtraction(self, 4, 2) == 2  # 4 - 2 = 2

    def test_substraction_calculation_failed(self): # fail_test "-"
        assert self.calc.subtraction(self, 4, 2) == 3 # 4 - 2 != 3

    def test_adding_calculate_correctly(self): #test "+"
        assert self.calc.adding(self, 2, 2) == 4 # 2 + 2 = 4

    def test_adding_calculation_failed(self): #fail_test "+"
        assert self.calc.adding(self, 2, 2) == 5 # 2 + 2 != 5

    def test_division_calculate_correctly(self): #test "/"
        assert self.calc.division(self, 4, 2) == 2 # 4 / 2 = 2

    def test_division_calculation_failed(self): #fail_test "/"
        assert self.calc.division(self, 4, 2) == 5 # 4 / 2 != 5
        



