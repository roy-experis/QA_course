a = int(input("enter positive num"))       #תרגיל 1
b=a
while a!=0:
    if 0 <= a < b:
        b=a
    a = int(input("enter positive num"))
print(b)
