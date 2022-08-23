Dic1 ={1:10 , 2:20}
Dic2 ={3:30 , 4:40}
Dic3 ={5:50 , 6:60}
NewDic ={}
NewDic2 = Dic1 | Dic2 | Dic3
NewDic.update(Dic1)
NewDic.update(Dic2)
NewDic.update(Dic3)
print(NewDic)
print(NewDic2)
