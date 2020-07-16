a = int(input("enter positive num"))
b=a
count= 0
while a>0:
    count=count +1
    a=a//10
if count==3:
    a=0
    while b > 0:
         a = a + b % 10
         b=b//10
    print("sum=",a)