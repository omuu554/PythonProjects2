

def FuzzyMath(Num1 , Num2 , operator):
    RaiseExpIfNotNumbers(Num1, Num2)

    Result = FuzzyOperatorResult(Num1, Num2, operator)

    if(Result < 0):
        return 'A negative number, what does that even mean'
    elif(Result < 10):
        return 'A small number. i can deal with that'
    elif(Result < 20):
        return 'A medium number. ok'
    else:
        return 'A big number, way to big for me'



def IsAddOperator(operator):
    if(operator == '+'):
        return True
    return False

def IsMultiOperator(operator):
    if(operator == '*'):
        return True
    return False

def SumFunction(Num1, Num2):
    return Num1 + Num2

def MultiFunction(Num1, Num2):
    return Num1*Num2

def RaiseExpIfNotNumbers(Num1 , Num2):
    if (type(Num1) != int or type(Num2) != int):
        raise Exception("We need ints to do fuzzy maths")

def FuzzyOperatorResult(Num1, Num2, operator):
    if (IsAddOperator(operator)):
        Result = SumFunction(Num1, Num2)
        return Result
    elif (IsMultiOperator(operator)):
        Result = MultiFunction(Num1, Num2)
        return Result
    else:
        raise Exception(f"I dont know how to do math with this '{operator}'")


