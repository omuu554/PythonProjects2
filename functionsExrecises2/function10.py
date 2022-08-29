


def GetSet(List:list):
    ListNew = []
    for Element in List:
        if Element not in ListNew:
            ListNew.append(Element)

    return ListNew



List = [12,5,4,6,88,9,2,3,4,4,2,21,34,22,78,32,2,21,32,54,767,15]

print(GetSet(List))