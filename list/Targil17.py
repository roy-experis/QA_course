list1=[int(input("Enter a new number: ")) for i in range(10)]
list2=[int(input("Enter a new number: ")) for i in range(16)]
for i in list1:
    if i in list2:
        print("Yes")
        break
else:
    print("No")