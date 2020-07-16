a = int(input("enter positive num"))     #תרגיל 2
count= 0
while a>0:
    count=count +1
    a=a//10
if count==3:
    print("המספר הוא תלת ספרתי")
else:
    print("error")