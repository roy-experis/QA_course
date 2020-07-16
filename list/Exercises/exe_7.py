list=[]
newList=[]
a=0
for i in range(1,11):
    list.append(i)
print(list)
while(a<len(list)):
    if(list[a]%2==1):
        newList.append(list[a])
    a=a+1
print(newList)