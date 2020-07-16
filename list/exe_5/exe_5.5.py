x=[]
y=int(input("enter list of grads"))
fail=0
pas=0
while 0 < y < 100:
    if y>59:
        pas=pas+1
    else:
        fail=fail+1
    x=x+[y]
    y=int(input("enter list of grads"))
print(x)
print(pas,"passed the exam")
print(fail,"students fail the exam")