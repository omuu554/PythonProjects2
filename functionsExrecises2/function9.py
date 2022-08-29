

def GetItems(Dict:dict):
    List = []
    for keys in Dict:
        List.append((keys,Dict[keys]))

    return List


Dicitionay = {"1": 1, "bob":2 ,"3":3}
print(GetItems(Dicitionay))