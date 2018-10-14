data = input("Please enter a string, I will extract all the number from it:")
res=""

for c in data:
    if(c in "1234567890"):
        res+=c
print(res)

