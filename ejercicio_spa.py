print("\n---welcome to the spa---\n1. massage\n2. facial\n3. manicure")
service1={"1":"massage","2":"facial","3":"manicure"}
def service():
    try:
        service_1=int(input("please enter your service: "))
        if  service_1<0:
            print("service not valid please try again")
            return service()        
        else:
            return service_1
    except ValueError:
        print("letters don`t alow please try again")
        return service()
op=service()

if op==1:
    print(f"your service is {service1.get('1')}")
elif op==2:
    print(f"your service is {service1.get('2')}")
elif op==3:
    print(f"your service is {service1.get('3')}")
else:
    print("service not available")