from random import *
def my_len (list):
    i=0
    for i in list:
        i=i+1
    return i-1

def my_count (list, num):
    i=0
    count=0
    while(i<len(list)):
        if(list[i]==num):
            count=count+1
        i=i+1
    return count

def my_find (list, num):
    i=0
    while(i<len(list)):
        if(list[i]==num):
            return i
        i=i+1
    return None

def my_max (list):
    i=0
    max=list[i]
    while(i<len(list)):
        if(list[i]>max):
            max=list[i]
        i=i+1
    return max