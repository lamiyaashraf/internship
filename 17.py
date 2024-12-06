a=int(input("enter the number="))
b=int(input("enter the number="))
lst=['add','sub','mul','div','exit']
print('1-addition  2-subtraction  3-multiplication  4-division  5-exit')
n=1
for n in lst:
    n=int(input("select the operation to be performed-"))
    if n==1:
        print("addition")
        c=a+b
        print(c)
    if n==2:
        print("subtraction")
        c=a-b
        print(c)
    if n==3:
        print("multiplication")
        c=a*b
        print(c)
    if n==4:
        if a==0 or b==0:
           print ("operation cannot be performed")
        else:
            print("division")
            c=a/b
            print(c)
    if n==5:
        print("stopped")


