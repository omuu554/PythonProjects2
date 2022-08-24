import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def GetAcendingDic(Dictionary):
    DicFake = Dictionary.copy()
    DicFake = dict(sorted(DicFake.items(),key= operator.itemgetter(1)))
    return DicFake

def GetDecendingDic(Dictionary):
    DicFake = Dictionary.copy()
    DicFake = dict(sorted(DicFake.items(),key= operator.itemgetter(1), reverse=True))
    return DicFake




print(GetAcendingDic(d))
print(GetDecendingDic(d))