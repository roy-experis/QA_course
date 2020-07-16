a=int(input("enter grade or 1 to stop"))
sum=0
avg=0
while a!=1:
    if 0 <= a <= 100:
        a = int(input("enter grade or 1 to stop"))
        sum=sum+1
        avg=avg+a
    else:
        a = int(input("wrong grade please enter again"))
print(avg/sum,"average grade is")