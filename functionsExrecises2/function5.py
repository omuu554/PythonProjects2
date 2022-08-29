

def WhatType(Itiratable):
    if(type(Itiratable) == dict or type(Itiratable) == str or type(Itiratable) == set or type(Itiratable) == tuple):
        return True
    return False


def ConvertToList(Itiratable):
    List = []
    if(WhatType(Itiratable)):
        for Elements in Itiratable:
            List.append(Elements)
        return List
    raise Exception("Not a good Itiratable Object")


List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]
Dicitionay = {"1": 1, "2":2 ,"3":3}
Set = set(List)


print(ConvertToList(Tuple))

