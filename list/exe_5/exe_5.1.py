a = int(input("enter positive num"))
sum=0
count=0
small=a
big=a
x=[]
while a!=0:
    x=x+[a]
    if a>big:
        big=a
    if a<small:
        small=a
    sum=sum+a
    count=count+1
    a = int(input("enter positive num or 0 to stop"))
print("the smallest num is",small)
print("the biggest num is",big)
print("the average is",(sum/count))