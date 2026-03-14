def name():
        name_1=input("please enter your name: ")
        if not name_1.isalpha():
            print("name not valid please try again")
            return name()        
        else:
            return name_1    
def product():
    try:
        product_1=int(input("please enter the product what do you want: "))
        if  product_1<=0:
            print("product not valid please try again")
            return product()
        else:
            return product_1
    except ValueError:
        print("letters don`t alow please try again")
        return product()  
def option():
    try:
        option_1=int(input("what do you want to do?: "))
        if  option_1<=0:
            print("option not valid please try again")
            return option()
        elif option_1>3:
            print("option not valid please try again")
        else:
            return option_1
    except ValueError:
        print("letters don`t alow please try again")
        return option() 
def many():
    try:
        many_1=int(input("how many products do you want?: "))
        if  many_1<=0:
            print("option not valid please try again")
            return option()        
        else:
            return many_1
    except ValueError:
        print("letters don`t alow please try again")
        return many() 

order=[]
while True:
    print("\n---menu---\n1. add a order\n2. total user register\n3. exit")
    op_1=option()
    if op_1==1:
        print("\n---welcome to the ice cream shop---\n1. cone $3000\n2. cup $4000\n3. banana split $9000")
        name_1=name()
        op = str(product())
        can=many()
        opti={"1":3000,"2":4000,"3":9000}        
        order.append({"name":name_1,"order":opti.get(op),"many":can})
        print("\n---available products---")
        for p in order:
            sub_total=p["order"]*p["many"]
            print(f"{p["name"]}: ${p["order"]} your total is: {sub_total}")
    elif op_1==2:
        for i in order:
            total+=i["order"]*["many"]
            num_1=len(order)
            print(f"the total of the day is: {total}")
            print(f"all the ordes in the day is: {num_1}")
    elif op_1==3:
        break




