print("SIMPLE CALCULATOR !!!")
while True:
    print("1. Do you want to add 2 numbers")
    print("2. Do you want to multiply 2 numbers")
    print("3. Do you want to subtract 2 numbers")
    print("4. Do you want to divide 2 numbers")
    print("5 . Exit ")
    print("Please enter your choice: ")
    a = input()
    if int(a) == 1:
        var1 = int(input("Please enter first number"))
        var2 = int(input("Please enter second number"))
        print("The result is: ", var1 + var2)
        print("")
        continue
    elif int(a) == 2:
        var1 = int(input("Please enter first number"))
        var2 = int(input("Please enter second number"))
        print("The result is: ", var1 * var2)
        print("")
        continue
    elif int(a) == 3:
        var1 = int(input("Please enter first number"))
        var2 = int(input("Please enter second number"))
        print("The result is: ", var1 - var2)
        print("")
        continue
    elif int(a) == 4:
        var1 = int(input("Please enter first number"))
        var2 = int(input("Please enter second number"))
        print("The result is: ", var1 / var2)
        print("")
    elif int(a) == 5:
        print("Exiting the program. Thank you !!!")
        break
