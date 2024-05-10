menu={
   
    'lemon juice': 50,
    'orange juice': 50,
    'water': 50,
    'burger': 150,
    'pizza': 200,
    'pasta': 170,
    'ice cream': 100,
    'ice tea': 100,
    'coke': 100,
    'pepsi': 100,
}
name = input("Please enter your name :")
gen = input("Please enter your gender :")
order_total = 0

if gen == "male":
    print(f"Welcome {name} to our restaurant sir!!")
else:
    print(f"Welcome {name} to our restaurant ma'am!!")
print("Would you like to have our menu? y/n")
ans = input("Enter your response :")
if ans == "yes":
    print(f"What do you want {name}?....Starter,Main, Dessert or Drinks?")
    res = input("Enter your response:")
    if res == "Starter":
        print("1.lemon juice\n2.orange juice\n3.Water")
    elif res == "Main":
        print("1.burger\n2.pizza\n3.pasta")
    else:
        print("1.ice cream\n2.ice tea\n3.coke\n4.pepsi")    
        
else:
    print(f"Thank you {name} for visiting our restaurant!!")

item_1 = input("Enter your item  please: ")
if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"You have ordered {item_1}")
    print("Would you like to have anything more?")
    res1 = input("Please enter your response: (y/n) ")
    if res1 == "yes":
        item_2 = input("Enter your item please:")
        if item_2 in menu:
            order_total = order_total + menu[item_2]
            print(f"You have ordered {item_2} and {item_1}")
            print("Would you like to have anything more?")
            res3 = input("Please enter your response: (y/n) ")
            if res3 == 'yes':
                item_3 = input("Enter your item please:")
                if item_3 in menu:
                    order_total = order_total + menu[item_3]
                    print(f"You have ordered {item_3},{item_2} and {item_1}")
                    print(f"Your total bill is {order_total}")
                    print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")
                    
                    
                else:
                    print("sorry we dont have that item")
                    print(f"Your total bill is {order_total}")    
                    print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")
            else:
                print(f"Your total bill is {order_total}")
                print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")
        else:
            
            print(f"Your total bill is {order_total}")    
            print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")  
    else:
        print("sorry we dont have that item")
        print(f"Your total bill is {order_total}")    
        print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")     
else:
    print("sorry we dont have that item, It will soon be in our menu")    
    print(f"Thank you {name} for visiting our restaurant!!  VISIT AGAIN!!")                 
                        
    
    
                

    