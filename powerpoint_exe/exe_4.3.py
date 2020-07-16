from random import randint
a=int(input("guess num"))      #תרגיל 4.3
b=(randint(1,10))
count=1
while a!=b:
    if a>b:
        a = int(input("guess again, to high"))
        count=count+1
    else:
        a = int(input("guess again, to low"))
        count = count + 1
if count==1:
    print("correct!, you have tried", count, "time")
else:
    print("correct!, you have tried", count,"times")

