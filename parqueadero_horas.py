def hours():
    try:
        hours_1=int(input("please enter your total hours in parking: "))
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
hours_2=hours()
print("\nremeber\nfirst hour: $5000\nall them :3000")
if hours_2==1:
    print("your total is $5000")
else:
    hours_1=(hours_2-1)*3000    
    total_hours=hours_1+5000
    print(f"your total to pay is {total_hours}")