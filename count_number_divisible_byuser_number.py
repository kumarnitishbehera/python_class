n=int(input("enter the number  with which you want to divide: "))
r=int(input("enter the number  till which you want to do division: "))

c=0
print("The even numbers are: ")
for i in range(0,r):
   if(i%n==0):
       c+=1

print("{} number in the range ( 0, {}), are divisible by {}".format(c,r,n))

