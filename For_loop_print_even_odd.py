n=int(input("enter the number till whihc you want to find  odd and even number : "))
print("The even numbers are: ")
for i in range(0,n):
   if(i%2==0):
        print(i)

print("The odd numbers are : ")
for i in range(0,n):
    if (i%2 != 0):
        print(i)