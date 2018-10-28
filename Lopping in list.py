mylist=[4,7,10,79,100]

for i in range(0, len(mylist)):
    if mylist[i]%10==0:
        print(mylist[i])

#extract all the element
print("*"*50)
for i in range(0,len(mylist)):
    print(mylist[i])
print("$"*50)
for x in mylist:
    print(x)
