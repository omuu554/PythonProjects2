

def GetListLenth(List:list):
    count = 0
    ListFake = List.copy()
    while(ListFake):
        ListFake.pop()
        count += 1

    return count


List = [1,2,3,"abc","123",12,"dad",["ron",123],233]
print(GetListLenth(List))

