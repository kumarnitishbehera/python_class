n=int(input("pleae find a number to find if its prime or not :"))

prime=1
i=2
while (True):
    if(n%i==0):
        prime=0
        break;
    i+=1
    if(i==(n-1)):
        break;


if prime==1:
    print("The number is  PRIME !!!!")
else:
    print("The number is NOT PRIME !!!!!!!!!")
