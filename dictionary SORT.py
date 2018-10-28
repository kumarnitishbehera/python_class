fruits={"orange":"a sweet ans sour fruit",
        "apple":"good for health",
        "leamon":"has vitamin c in it",
        "carrot":"used as a salad",
        "mango" :"best summer fruit"
        }
listofkeys=list(fruits.keys())
print(listofkeys)
print("XX"*50)

for x in sorted(listofkeys):
    print(x,":",fruits[x])

print("XX"*50)

listofkeys.sort()

for key in listofkeys:
    print(key,";", fruits[key])