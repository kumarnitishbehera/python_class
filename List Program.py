fruit_list= []
while True:
    fruit_name=input("Please enter a fruit: ")
    if fruit_name == "exit":
        break
    fruit_list.append(fruit_name)

item=input("which fruit are you looking for : ")
if item in fruit_list:
    print("Fruit is present !!!")
else:
    print("Fruit is nor present !!!!")

print(fruit_list)