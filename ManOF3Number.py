a=int(input("enter the first number :"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
if(b>c):
    print(b)
else:
    print(c)