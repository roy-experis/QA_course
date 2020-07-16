a=int(input("enter day"))      #תרגיל 7
b=int(input("enter month"))
c=int(input("enter year"))
if 0<a<32 and 0<b<13 and 1949<c<2021:
    print(a,"/",b,"/",c%100)
elif 1>a or a>31:
    print("invalid day")
if 1>b or b>12:
    print("invalid month")
if 1950 >c or c > 2020:
    print("invalid year")