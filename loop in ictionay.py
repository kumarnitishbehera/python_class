fruits={"orange":"a sweet ans sour fruit",
        "apple":"good for health",
        "leamon":"has vitamin c in it",
        "carrot":"used as a salad",
        "carrot" :"can be used in many dishes",
        "mango" :"best summer fruit"
        }
for key in fruits:
    print("{}, {}".format(key,fruits[key]))

for val in fruits.values():
    print(val)

for key,val in fruits.items():
    print(key)
    print(val)