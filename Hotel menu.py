#Hotel Menu

menu=[]
dish1=[1,"egg curry",34.5,["egg","onion","chilly"]]
dish2=[2,"pasta",60.5,["egg","noodles","curry"]]
dish3=[3,"Mashed Potato",144.5,["potato","onion","chilly"]]
dish4=[4,"Salad",55.5,["carrot","radish","potato"]]
dish5=[5,"chapati",66.5,["wheat","salt"]]

menu.append(dish1)
menu.append(dish2)
menu.append(dish3)
menu.append(dish4)
menu.append(dish5)

item = input("please tell me what do you like?")

for dish in menu:
    if item in dish[3]:
        print(dish[1])

price = float(input("please enter the price you want to see :"))

for dish in menu:
    if price > dish[2]:\
        print(dish[1])

