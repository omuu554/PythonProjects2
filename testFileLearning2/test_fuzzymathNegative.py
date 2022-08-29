from FuzzyMathFunction import *
import unittest

import pytest




class Test_FuzzyMathNegative(unittest.TestCase):

    def setUp(self):
        self.Num1 = 12
        self.Num2 = 12


    def test_NoneIntNum1Exp(self):
        with pytest.raises(Exception) as exp:
            RaiseExpIfNotNumbers(str(self.Num1), self.Num2)
        assert str(exp.value) == "We need ints to do fuzzy maths"


    def test_NoneIntNum2Exp(self):
        with pytest.raises(Exception) as exp:
            RaiseExpIfNotNumbers(self.Num1, str(self.Num2))
        assert str(exp.value) == "We need ints to do fuzzy maths"



    def test_IsOperatorSomethingElseExp(self):
        with pytest.raises(Exception) as exp:
            FuzzyOperatorResult(self.Num1, self.Num2, '-')
        assert str(exp.value) == "I dont know how to do math with this '-'"


