from random import randint
a=int(input("enter num between 1-100"))      #תרגיל 4.4
b=(randint(1,100))
c=100
d=1
count=1
while a!=b:
    if a>b:
        d=b
        print(b)
        b=(randint(d,c))
        count=count+1
    else:
        c=b
        print(b)
        b=(randint(d,c))
        count=count+1
if count == 1:
    print("correct!, you have tried", count, "time")
else:
    print("you have tried for",count,"times")