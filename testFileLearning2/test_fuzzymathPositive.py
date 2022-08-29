from FuzzyMathFunction import *
import unittest


class Test_FuzzyMathPositive(unittest.TestCase):

    def setUp(self):
        self.operatorAdd = '+'
        self.operatorMultiply = '*'
        self.Num1 = 4
        self.Num2 = 4

    def tearDown(self):
        pass


    def test_IsOperatorIsAdd(self):
         self.assertTrue(IsAddOperator(self.operatorAdd))

    def test_IsOperatorIsMultiplyer(self):
        self.assertTrue(IsMultiOperator(self.operatorMultiply))

    def test_AddCorrectResult(self):
        self.assertEqual(FuzzyOperatorResult(self.Num1, self.Num2, self.operatorAdd), 8)

    def test_MultiplyCorrectResult(self):
        self.assertEqual(FuzzyOperatorResult(self.Num1, self.Num2, self.operatorMultiply), 16)

    def test_AdditionNegativeResult(self):
        Num1 = -5
        assert ("negative number" in FuzzyMath(Num1 ,self.Num2, self.operatorAdd))

    def test_AdditionSmallResult(self):
        assert ("small number" in FuzzyMath(self.Num1, self.Num2, self.operatorAdd))

    def test_AdditionMediumResult(self):
        Num1 = 10
        assert ("medium number" in FuzzyMath(Num1 ,self.Num2, self.operatorAdd))

    def test_AdditionBigResult(self):
        Num1 = 20
        assert ("big number" in FuzzyMath(Num1, self.Num2, self.operatorAdd))

    def test_MultiplicationNegativeResult(self):
        assert ("negative number" in FuzzyMath(-1*(self.Num1), self.Num2, self.operatorMultiply))

    def test_MultiplicationSmallResult(self):
        Num1 = 2
        assert ("small number" in FuzzyMath(Num1, self.Num2, self.operatorMultiply))

    def test_MultiplicationMediumResult(self):
        assert ("medium number" in FuzzyMath(self.Num1, self.Num2, self.operatorMultiply))

    def test_MultiplicationBigResult(self):
        assert ("big number" in FuzzyMath(self.Num1*2, self.Num2, self.operatorMultiply))






