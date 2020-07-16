a = int(input("enter age"))
while a>0:
    if a<=18:
        print("child")
    elif a<=60:
        print("adult")
    elif a<=120:
        print("senior")
    a = int(input("enter age"))