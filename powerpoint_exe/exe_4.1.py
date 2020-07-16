a=int(input("enter big positive num"))      #תרגיל 4.1
b=int(input("enter small positive num"))
if a%2==0:
    a=a-2
    while a>0:
        print(a)
        a=a-2
else:
    a=a-1
    while a>0:
        print(a)
        a=a-2
if b%2==0:
    b=b-2
    while b>0:
        print(b)
        b=b-2
else:
    b=b-1
    while b>0:
        print(b)
        b=b-2