n=int(input("pleae find a number to find if its prime or not :"))

prime=1

for i in range(2,n):
    if(n%i==0):
        prime=0
        break;

if prime==0:
    print("the number is  PRIME !!!!")
else:
    print("the number is NOT PRIME !!!!!!!!!")
