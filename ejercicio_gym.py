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
def age():
    try:
        age_1=int(input("please enter your age: "))
        if  age_1<13:
            print("age not valid ")
            
        elif age_1>=13:
            print("age valid, your class is teen class ")
            
        elif age_1>=59:
            print("age valid, your class is general class ")
        else:
            print("age valid, your class is sennior class ")
    except ValueError:
        print("letters don`t alow please try again")
        return age()
name()
age()