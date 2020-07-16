from random import randint
x=(randint(0,100))
str=[]
a=0
while a!=10:
    str=str+[x]
    a=a+1
    x = (randint(0, 100))
print(str[:])