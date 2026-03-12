def age():
    try:
        age_1=int(input("please enter your age: "))
        if  age_1<=0:
            print("age not valid please try again")
            return age()
        else:
            return age_1
    except ValueError:
        print("letters don`t alow please try again")
        return age()        
age_1=age()
if age_1<12:
    print("you have to pay $8000")
elif age_1<59:
    print("you have to pay $12000")
else:
    print("you hace to pay $9000")