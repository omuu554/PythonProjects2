


def GetValues(Dict:dict):
    List = []
    for keys in Dict:
        List.append(Dict[keys])

    return List


Dicitionay = {"1": 1, "bob":2 ,"3":3}
print(GetValues(Dicitionay))