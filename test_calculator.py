
import pytest
from data import EXTRACT_TEST_DATA
from data import SUM_TEST_DATA
from calculator import Calculator
from helpers import generate_random_number

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2,3) == 6

class TestCalculator:
    
    def test_extract(self):
        calc = Calculator()
        assert calc.extract(5,3) == 2
    
    @pytest.mark.parametrize('a, b, expected_result', [(2, 3, 5),
        (0, 0, 0), 
        (-1, 1, 0), 
        (-2, -3, -5), 
        (1.0, 2.5, 3.5)])
# 'a, b, result' названия переменных
# Первый аргумент должен быть либо строкой с именами параметров, либо кортежем/списком имён. 
# Второй аргумент — список значений (итератор) для этих параметров.
    def test_sum(self, calculator, a, b, expected_result): # тест с фикстурой
        assert calculator.sum(a,b) == expected_result, f"This test failed, because {a} + {b} != {expected_result}" # после запятой можно добавить сообщение об ошибке

    @pytest.mark.parametrize('a, b', [
        *SUM_TEST_DATA,
        (generate_random_number(-1000,1000), generate_random_number(-1000,1000))])
# 'a, b, result' названия переменных
# Первый аргумент должен быть либо строкой с именами параметров, либо кортежем/списком имён. 
# Второй аргумент — список значений (итератор) для этих параметров.
    def test_sum(self, calculator, a, b): # тест с фикстурой
        assert calculator.sum(a,b) == a+b, f"This test failed, because {a} + {b} != expected_result"

    @pytest.mark.parametrize('a,b', 
                             EXTRACT_TEST_DATA)
    def test_extract(self, calculator, a,b):
        assert calculator.extract(a,b) == a-b

    #def test_sum(self, calculator): # тест с фикстурой
     #   assert calculator.sum(2,3) == 5


