def name():
        name_1=input("please enter the name product: ")
        if not name_1.isalpha():
            print("name not valid please try again")
            return name()        
        else:
            return name_1    
def price():
    try:
        price_1=int(input("please enter the products price: "))
        if  price_1<=0:
            print("price not valid please try again")
            return price()
        else:
            return price_1
    except ValueError:
        print("letters don`t alow please try again")
        return price()      
products=[]
for r in range(6):
    name_1=name()
    price_1=price()    
    products.append({"name":name_1, "price": price_1})
print("\n---available products---")
for p in products:
    print(f"{p["name"]}: ${p["price"]}")
max_price=[i for i in products if i["price"]>=100000]
for i in max_price:
    print(f"\n---products greater than $100.000---")
    print(f"\n{i['name']}: ${i['price']}")