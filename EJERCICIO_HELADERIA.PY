def name():
    try:
        name_1=input("please enter your name: ")
        if not name_1.isalpha():
            print("name not valid please try again")
            return name()        
        else:
            return name_1
    except ValueError:
        print("numbers don`t alow please try again")
        return name()
def flavor_s():
    try:
        flavor=int(input("please chose a flavor: "))
        if  flavor<0:
            print("flavor not valid please try again")
            return flavor_s()
        elif flavor>3:
            print("flavor not valid please try again")
            return flavor_s()
        else:
            return flavor
    except ValueError:
        print("letters don`t alow please try again")
        return flavor_s()

ice_cream=[]
name()
for i in range(5):
    print("\n alowed flavors\n 1. vanilla\n 2. strawberry\n 3. chocolate\n")
    flavor=flavor_s()
    if flavor==1:
        ice_cream.append("vanilla")
    elif flavor==2:
        ice_cream.append("strawberry")
    elif flavor==3:
        ice_cream.append("chocolate")


vanilla=ice_cream.count("vanilla")
strawberry=ice_cream.count("strawberry")
chocolate=ice_cream.count("chocolate")
print(f"\nvanilla apears {vanilla} times\nstrawberry apears {strawberry} times\nchocolate apears {chocolate} times\n")