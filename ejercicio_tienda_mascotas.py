print("\n-----tienda-----\n1. Dog\n2. Cat\n3. Bunny\n")
products={"1":"Dog","2":"Cat","3":"Bunny"}
def animal():
    try:
        proct=int(input("what pet do you have?: "))
        if  proct<0:
            print("item not valid please try again")
            return animal()
        elif proct>3:
            print("item not valid please try again")
            return animal()
        else:
            return proct
    except ValueError:
        print("letters don`t alow please try again")
        return animal()
pet=animal()
if pet==1:
    print(f"")