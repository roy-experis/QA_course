a=int(input("enter grade"))      #תרגיל 4
avg=0
sum=0
error=0
while error<5:
    while 0 <= a <= 100 and sum < 9:
        avg=avg+a
        sum=sum+1
        a = int(input("enter grade"))
        error=0
    error=error+1
    if sum != 9:
        a = int(input("error, enter grade"))
if sum==9:
    print("the average is", avg/sum)
else:
    print("error")