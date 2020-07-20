from dictionaries.exe_1 import *
dicSum=create_dic()
print(dicSum)
key = int(input("enter wanted key"))
for i in dicSum.keys():
    print(i)
    if i==key:
        print("yes")
        break
    else:
        print("no")
create_dic()