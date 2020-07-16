a=int(input("enter length"))      #תרגיל 1
b=int(input("enter wide"))
c=a
d=b
while d>0:
    while c>0:
        print("*",end=' ')
        c=c-1
    print("")
    c=a
    d=d-1
