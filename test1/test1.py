b=int(input("enter num"))
if b>0:
    print("positive")
else:
    if b<0:
        print("negative")
    else:
        print("zero")
        while b > 0:
            b=b-1
c = int(input("enter positive num"))
count= 0
while c>0:
    count=count +1
    c=c//10
if count==1:
    print("המספר הוא חד ספרתי")
else:
    if count ==2:
        print("המספר הוא דו ספרתי")
    else:
        if count == 3:
            print("המספר הוא תלת ספרתי")
        else:
            print("המספר מורכב מ-" ,count," ספרות")