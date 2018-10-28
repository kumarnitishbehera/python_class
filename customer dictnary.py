customer={}

cust1=["mukund",20,"HSr",{
                        1:[[444,"moto e4",10000,1],[555,"blackshit",1000,4],[666,"TV",20000,1]]
                        2:[[222,"cricket bat",400,3],[777,"tennis ball",100,10]]
},"prime"]


cust2=["john",50,"kormangala",{
                        1:[[22,"washing machine",20000,2],[33,"shoes",900,4],[44,"vegetable",20,1]]
                        2:[[567,"bet",1400,3],[788,"car wash",800,10]],
                        3:[[890,"sofa set",50000,1]]
},"not prime"]


customer[1234]=cust1
customer[12345]=cust2

phone=int(input("what is your phone number:"))

shopping_list_key_1=1
if phone in customer:
    shopping_dict =customer[phone][3]
    if shopping_list_key_1 in shopping_dict:
        item1=shopping_dict[shopping_list_key_1]
    else:
        print