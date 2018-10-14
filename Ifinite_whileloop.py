
#infinite while loop
while(True):
    x = int(input("Please input the number :"))
    n = int(input("please enter any random number : "))
    if(n%x==0):
        print("the number {} is divisible by {}".format(n,x))
        break;
