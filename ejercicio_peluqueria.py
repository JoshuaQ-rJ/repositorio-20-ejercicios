def hours():
    try:
        hours_1=int(input("please enter your time arrive: "))
        if  hours_1<0:
            print("hour not valid please try again")
            return hours()
        elif hours_1>23:
            print("hour not valid please try again")
            return hours()
        else:
            return hours_1
    except ValueError:
        print("letters don`t alow please try again")
        return hours()

hou=hours()
if hou>6:
    print("you are in the morning")
elif hou>=12:
    print("you are in the evening")
elif 18<=hou>=22:
    print("you are in the night")
else:
    print("the barber is not open")
