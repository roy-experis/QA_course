list=[]
newList=[]
for i in range(1,11):
    list.append(i)
print(list)
for i in range(1,11):
    list.append(i)
    if(i%3==0):
        newList.append(i)
        list.remove(i)
print(newList)