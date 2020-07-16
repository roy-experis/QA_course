list=[1,1]
for i in range(3,11):
    a=len(list)
    while(a>=0):
        list.append(sum(list))
        a=a-1
print(list)
