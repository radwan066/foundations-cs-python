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
        choice=(input("Please enter a number(1->9):"))
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