from project1.help_function import *
# a=int(input('enter 3 digit number'))
# print(sum_digits(a),"sum_digits")
# print(num_is_3_digits(a))
#
# a=int(input('enter number of times you want to print the string'))
# str=input('enter the wanted string')
# print_a_times_the_string(str,a)
# print(sum_fibonachi(a),"sum_fibonachi")
#
# for i in range (5):
#     a = int(input('enter number you want fibonachi'))
#     print(sum_fibonachi(a), "=sum_fibonachi",i+1)

# a = int(input('enter lower number of range'))
# b = int(input('enter upper number of range'))
# print(number_betwin_range1(a,b))
# a = int(input('enter number 1'))
# b = int(input('enter number 2'))
# if(a>=b):
#     print(number_betwin_range1(b, a))
# else:
#     print(number_betwin_range1(a, b))
# a = int(input('enter number'))
# b = int(input('enter number you enter to pow'))
# number_pow(a,b)
# for i in range (5):
#     a = int(input('enter age'))
#     age_group(a)
# for i in range(5):
#     a = int(input('enter grade'))
#     if(check_grade(a)==True):
#         print('the student pass the exam')
#     else:
#         print('the student did nit pass the exam')
# a=[]
# fill_positive_up_to_40(a)
# print(a)
# a=[]
# fill_between_1_and_100(a)
# print(a)
# b=int(input("enter num you want to check in the list"))
# check_how_many_in_a_list(a,b)
# max_in_list(a)
a = int(input("enter num of students"))
list_student=(class_grade(a))
print(list_student)
print(class_grade_avg(list_student))