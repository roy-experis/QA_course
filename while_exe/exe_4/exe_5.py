a=int(input("enter big positive num"))      #תרגיל 5
b=int(input("enter small positive num"))
if a>b:
    sum=0
    c=0
    while a>sum:
        sum=sum+b
        c=c+1
    print(sum % (sum-1), "שארית:")
    print(c-1,"מנת החילוק")
else:
    a = int(input("enter big positive num"))
    b = int(input("enter small positive num"))
