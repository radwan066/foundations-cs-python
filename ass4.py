cities=["nabatiye","saida","beirut","byblos","tripoli"]
drivers={}
drivers["salim"]=["saida","nabatiye"]
drivers["houssam"]=["saida","beirut"]
drivers["jad"]=["saida","beirut","byblos"]
drivers["majd"]=["byblos","tripoli"]
drivers["lama"]=["nabatiye","byblos"]
def check(city):
    list=[]
    if city in cities:
      for key,value in drivers.items():
        if city in value:
          list.append(key)
    print(list)       
def remove_city(driver,city):
  if city in cities:
    if driver in drivers:     
     for i in range(len(drivers[driver])):
       if drivers[driver][i].lower()==city.lower():
         drivers[driver].pop(i) 
         break
def add_route(driver,city):
  if city.lower() in cities:
    if driver.lower() in drivers:
      print("enter:")
      print("0.To add to the beginning of the route")
      print("-1.To add to the end of the route")
      print("#. (any other number) to add that city to the given index")
      choice=int(input("enter your choice: "))
      if choice==0:
        drivers[driver].insert(0,city)
      elif choice==-1:
        drivers[driver].append(city)
      elif choice>0 and choice<len(drivers[driver]):
        drivers[driver].insert(choice,city)
    else :
      print("you didn't add this driver")
  else :
    print("you didn't add this city")
def add_driver(driver):
    if driver.isnumeric():
      print("please enter a valid driver")
    elif driver not in drivers:
      drivers[driver]=[]
    else:
      print("this driver already exists")
      print(drivers)  
def add_city(city):
  if city.isnumeric():
    print("please enter a valid city" )
  else:  
   if city.lower() not in cities:
      cities.append(city)    
  print(cities)
def mainMenu():
    choice=0
    while choice!=6:
     print("Enter")
     print("1.to add a city")
     print("2.to add a driver")
     print("3.To add a city to the route of a driver") 
     print("4.Remove a city from a driver’s route")
     print("5.To check the deliverability of a package")
     print("6.to close the program")
     choice=int(input("enter a number"))
     if choice==1:
        print("adding new city...")
        city_to_add=input("add the new city: ")
        add_city(city_to_add)
     elif choice==2:
        print("adding new driver...")
        driver_to_add=input("add the new driver: ")
        add_driver(driver_to_add)     
     elif choice==3:
        print("adding a city to the route of a driver...")
        driver=input("enter the name of the driver: ")
        city=input("enter the name of the city: ")
        add_route(driver,city)
        print(drivers)
     elif choice==4:
        print("removing a city from a driver's route...")  
        x=input("enter the name of the driver: ")
        y=input("enter the name of the city: ")
        remove_city(x,y)
        print(drivers)
     elif choice==5:
        print("checking deliverability of a package...")
        z=input("enter the name of the city: ")
        check(z)
     elif choice==6:
        print("bye bye")
     else :
         print("invalid input!")
mainMenu()                  
