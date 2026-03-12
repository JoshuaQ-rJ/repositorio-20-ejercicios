def assistance():
    try:
        assistance_1=int(input("please enter your assistance this month: "))
        if  assistance_1<=0:
            print("assistance not valid please try again")
            return assistance()
        else:
            return assistance_1
    except ValueError:
        print("letters don`t alow please try again")
        return assistance()        
assistance_1=assistance()
if assistance_1<5:
    print("you have low assistance")
elif assistance_1<8:
    print("you have medium assistance" )
else:
    print("you have hiw assistance")