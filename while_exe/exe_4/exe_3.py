a = int(input("enter positive num"))      #תרגיל 3
count=1
big=a
num=count
while count<7:
    if big<a:
        num=count
        big=a
    count = count + 1
    a = int(input("enter positive num"))
print("the digit of the biggest num is:", num)