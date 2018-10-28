fruits={"orange":"a sweet ans sour fruit",
        "apple":"good for health",
        "leamon":"has vitamin c in it",
        "carrot":"used as a salad",
        "carrot" :"can be used in many dishes",
        "mango" :"best summer fruit"
        }
print(fruits)
fruits["mango"]="seasonal fruit, very popular"

print(fruits)

name=input("what fruit you like:")
print(fruits.get(name))
name=input("what fruit you like:")
if name in fruits:
    print(fruits[name])
else:
    print("fruit not found!!!!!!")



