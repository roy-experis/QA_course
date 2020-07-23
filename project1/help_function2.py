from random import *
def return_str_whithout_a_or_A (str):
    i=0
    newStr=""
    while(i<len(str)):
        if(str[i]!='a' and str[i]!='A'):
            newStr+= str[i]
        i=i+1
    return newStr

def return_reverse_str (str):
    i=len(str)-1
    newStr=""
    while(i>=0):
        newStr+= str[i]
        i=i-1
    return newStr

def return_first_and_last_char (str):
    i = 0
    newStr=str[0]
    newStr += str[len(str)-1]
    while (i <=len(str)):
        print(newStr)
        i=i+1
    return newStr

def return_if_num_is_prime(num):
    i=2
    count=0
    while(i<num//2+1):
        if(num%i==0):
            print(i)
            count=count+1
        i=i+1
    if(count==0):
        return "num is prime"
    else:
        return "num is not prime"

def return_rounded_num(num):
    if(num%1>=0.5):
        return (num//1+1)
    else:
        return (num // 1)

def return_discount(city,age):
    if(age<=10):
        return 0
    if(age<=18 and age>10 and city=="jerusalem"):
        return 0.5
    if (age <= 18 and age > 10):
        return 0.25
    if (age <= 60 and age > 18 and city == "jerusalem"):
        return 0.1
    if (age > 61):
        return 0.5
    else:
        return 1

def fill_random_between_a_and_b(upper,lower,num):
    a=0
    list=[]
    while(a<num):
        b=randint(lower,upper)
        print(b)
        list.append(b)
        a=a+1
    return ('the avrege is:',sum(list)/num)

def return_reverse_num (num):
    a=num
    i=1
    while(a!=0):
        i=i+1
        a=a//10
    newNum=0
    while(num!=0):
        newNum=newNum*10+ num%10
        num=num//10
    return newNum

def return_length_of_num (num):
    if(num==0):
        return 1
    if(num>0):
        i=0
        while(num != 0):
            i=i+1
            num=num//10
        return i
    else:
        num=num*-1
        i=0
        while (num != 0):
            i=i+1
            num=num//10
        return i