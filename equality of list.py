#equality of list

list1=[2,4,6]
list2=[4,2,6]

if list1==list2:
    print("two list are same !!!")
else:
    print("two list are not same!!!")


if sorted(list1)==sorted(list2):
    print("two list are same !!!")
else:
    print("two list are not same!!!")

list3=list1

if list1 is list3:
    print("address space is same")
else:
    print("address space is not same")

list3.append(8)
print (list1)

