def name():
    #i ask for the name and i validate with the method .isalpha that the name is a stringis not de code return
    name_1=input("please enter product's name: ")
    if not name_1.isalpha():
        print("invalid name please try again")
        return name()
    else:
        return name_1
def price():
    #i ask for the price and i validate with if and try,except
    try:
        price_1=int(input("pleas enter the price of the product: "))
        if price_1<=0:
            print(f" the {price_1} is not valid please try again")
            return price()
        else:
            return price_1
    except ValueError:
        print(" the price is not valid please try again")
        return price()
def amount():
    #i ask for the amount and i validate with if and try,except
    try:
        amount_1=int(input("please enter the amount of the products: "))
        if amount_1<=0:
            print(f" the {amount_1} is not valid please try again")
            return amount()
        else:
            return amount_1
    except ValueError:
        print(f" the {amount_1} is not valid please try again")
        return amount()
def option():
    try:
        option_1=int(input("what do you want to do?: "))
        if  option_1<=0:
            print("option not valid please try again")
            return option()
        elif option_1>4:
            print("option not valid please try again")
        else:
            return option_1
    except ValueError:
        print("letters don`t alow please try again")
        return option() 
inventory=[]
while True:
    print("\n---welcome to the inventory---\n1. add a product\n2. show inventory\n3. calculate inventory\n4. exit\n")
    op=option()
    if op ==1:
        name_1=name()
        price_1=price()
        amount_1=amount()
        inventory.append(product={"name":name_1,"price":price_1,"amount":amount_1})
    elif op ==2:
        print(f"the products register are:\n")
        for p in inventory:
            name_2=p["name"]
            price_2=p["price"]
            amount_2=["amount"]            
            print("products: {name_2}| price {price_2}| amount {amount_2}")
    elif op==3:
        total=0
        for i in inventory:
            total+= i["price"]*i["amount"]
            num=len(inventory)
        print(f"the total value for your inventory is: {total}\nthe total products register are: {num}")
    elif op ==4:
        print("leaving the inventory, thanks for your use")
        exit()