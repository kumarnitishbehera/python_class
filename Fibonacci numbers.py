print("Fibonacci numbers !!!")
userin =int(input("Please enter the number of Fibonacci numbers you want to print: "))
print("The ",userin ,"Fibonacci numbers are :")
print("0")
print("1")
userin-=2
a=0
b=1
for x in range(0,userin):
    c=a+b
    print(c)
    a=b
    b=c

