print('1-addition  2-subtraction  3-multiplication  4-division  5-exit')
n=int(input("select the operation to be performed-"))
if n==1:
    a=int(input("enter the number="))
    b=int(input("enter the number="))
    print("addition")
    c=a+b
    print(c)
if n==2:
    a=int(input("enter the number="))
    b=int(input("enter the number="))
    print("subtraction")
    c=a-b
    print(c)
if n==3:
    a=int(input("enter the number="))
    b=int(input("enter the number="))
    print("multiplication")
    c=a*b
    print(c)
if n==4:
        if a==0 or b==0:
           print ("operation cannot be performed")
        else:
            a=int(input("enter the number="))
            b=int(input("enter the number="))
            print("division")
            c=a/b
            print(c)
if n>=5:
     print("exit")
             
    
        