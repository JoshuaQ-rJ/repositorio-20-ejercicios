print("\n------cafe------\n1. coffy: $4000\n2. te: $3500\n3. juice: $5000\n")
products={"1":4000,"2":3500,"3":5000}
def product_s():
    try:
        proct=int(input("what do you want to drink?: "))
        if  proct<0:
            print("item not valid please try again")
            return product_s()
        elif proct>3:
            print("item not valid please try again")
            return product_s()
        else:
            return proct
    except ValueError:
        print("letters don`t alow please try again")
        return product_s()
def how_m():
    try:
        proct=int(input("how many drinks do you want?: "))
        if  proct<0:
            print("item not valid please try again")
            return how_m()
        else:
            return proct
    except ValueError:
        print("letters don`t alow please try again")
        return how_m()

proct=product_s()
proct_1=how_m()
if proct==1:    
    total=products.get("1")*proct_1
    print(f"Thanks for bought a coffy\nyour total is: {total}")
elif proct==2:
    total=products.get("2")*proct_1
    print(f"Thanks for bought a te\nyour total is: {total}")
elif proct==3:
    total=products.get("3")*proct_1
    print(f"Thanks for bought a juice\nyour total is: {total}")