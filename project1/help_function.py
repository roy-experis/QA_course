from random import *
def sum_digits(a):
    sum=0
    while(a!=0):
        sum=sum+a%10
        a=a//10
    return sum

def num_is_3_digits(a):
    count = 0
    while (a != 0):
        count=count+1
        a = a // 10
    if(count==3):
        return ('true')
    else:
        return ('false')

def print_a_times_the_string(str,a):
    while(a>=0):
        print(str)
        a=a-1

def sum_fibonachi(a):
    sum=0
    runner=a
    while(runner!=0):
        sum=sum+runner
        runner=runner-1
    return sum

def number_betwin_range1(a,b):
    while(b>=a):
        print(a,end=' ')
        a=a+1

# def number_betwin_range(a,b):
#     list1=[]
#     while(b>a):
#         list1.append(b)
#         b=b-1
#     return list1

def number_pow(a,b):
    count = 1
    while (b != 0):
        count = count*a
        b = b-1
    print(count)

def age_group(a):
    if(a>=0 and a<=18):
        print(a,'is a child')
    if (a >= 19 and a <= 60):
        print(a, 'is an adult')
    if (a >= 61 and a <= 120):
        print(a, 'is a senior')

def check_grade(a):
    if(a>=70 ):
        return (True)
    else:
        return (False)

def fill_positive_up_to_40(a):
    b=2
    while(b<=40):
        a.append(b)
        b=b+2
    return a

def fill_between_1_and_100(a):
    while(len(a)<=20):
        b=randint(1,100)
        a.append(b)

def check_how_many_in_a_list(list,b):
    print("the num is",list.count(b),"times in the list")

def max_in_list(list):
    print("max num is in the",list.index(max(list)),"index")

# def class_name_and_grade(a):
#     count=0
#     b=[]
#     while(count<a):
#         b.append(input("name of student"))
#         b.append(int(input("enter grade of student")))
#         count=count+1
#     return b

def class_grade(a):
    count=0
    list_students=[]
    while(count<a):
        b=int(input("enter grade"))
        list_students.append(b)
        count=count+1
    return list_students

def class_grade_avg(list):
    return (sum(list)/len(list))