print("User Input Program")
sum=0
while True :
    a=int(input(" Please enter a number (-1 to exit):"))
    if a== -1:
        print("Sum of all the number entered is : ", sum)
        break
    else:
        sum=sum+a