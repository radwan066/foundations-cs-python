openedtabs=[]


def Open_Tab():   #asking the user for the title and the url of the  website
    title=input("please enter the title of the tab:")
    if title and  title.isalnum(): #checking if title contains only alphabetics and numerical characters 
       url=input("please enter the URL:")
       if url and url.startswith(("www.","http:")): #checking if the url starts with www. or http 
         tabs={"title":title,"url":url}
         openedtabs.append(tabs)
       else :
          url=input("please enter the URL again:")
          Open_Tab()
    else :      
      print("please input a valid Title!")
      Open_Tab()     
    print(openedtabs)   
     
def Close_Tab():
    print(openedtabs)
    index=int(input("please,enter the index of the tabs you want to close:"))
    if openedtabs[index] in openedtabs:
        openedtabs.remove(openedtabs[index])
    else :
        openedtabs.pop()    
    print(openedtabs)

def mainmenu():
    choice=0
    while (choice!=9):
        print("1.Open Tab.")
        print("2.Close Tab.")
        print("3.Switch Tabs.")
        print("4.Display All Tabs.")
        print("5.Open Nested Tabs.")
        print("6.Sort All Tabs.")
        print("7.Save Tabs.")
        print("8.Import Tabs.")
        print("9.Exit")
        choice=int(input("Please enter a number(1->9):"))
        if (choice==1):
            Open_Tab()
        elif (choice==2):
            Close_Tab()
        elif (choice==3):
            Switch_Tabs 
        elif (choice==4):
            Display_All_Tabs()
        elif(choice==5):
            Open_Nested_Tabs()
        elif(choice==6):
            Sort_All_Tabs()
        elif(choice==7):
            Save_Tabs()
        elif(choice==8):
            Import_Tabs()
        elif(choice==9):
            print("Bye Bye!")
        else :
            print("Please enter a valid number!")      
mainmenu()