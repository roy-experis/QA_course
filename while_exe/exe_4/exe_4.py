a = int(input("enter positive num"))      #תרגיל 4
b=0
while a>0:
    b=b*10+a%10
    a=a//10
print("the number from the end to the start is:",b)
print(b*2)