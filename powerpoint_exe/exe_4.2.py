a=int(input("enter num"))      #תרגיל 4.2
b=2
c=0
while c==0 and b<a:
    if a%b==0:
        c=c+1
    else:
        b=b+1
if c!=0:
    print("המספר לא ראשוני")
else:
   print("המספר ראשוני")