from bs4 import BeautifulSoup
import requests
import json

openedtabs=[]

def Open_Tab():   #asking the user for the title and the url of the  website O(n) n:invalid title
    title=input("please enter the title of the tab:")
    while title and  title.isalnum(): #checking if title contains only alphabetics and numerical characters #O(n) n being the invalid title given by the user 
       url=input("please enter the URL:")
       while url and url.startswith(('www.','http:','https:')):    #O(1) giving two chances to the user to give a valid url 
            tabs={"title":title,"url":url}
            openedtabs.append(tabs)
            break
       else :
          url=input("please enter the url again or it won't be opened:")  
       break          
    else :      
      print("please input a valid Title!")
      Open_Tab()     
    print(openedtabs)   
     
def Close_Tab():  #first printing the list of the opened tabs than asking user for the index of the tab he wishes to close it #O(n) n:wrong index from the user
    y=(input("please,enter the index of the tabs you want to close:"))  
    if y.isdigit():
      index=int(y)
      if openedtabs[index] in openedtabs:   #searching for the index given by the user
        openedtabs.remove(openedtabs[index])
      else :                                #if the index is not in the list or its invalid the program will close the last opened tab
        openedtabs.pop()  
    else :
        print("you have to give us the index as integer!")  
        Close_Tab()    
    print(openedtabs)

def Switch_Tabs(): #first printing the list of the opened tabs than asking the user for the index of the tab in which he would see its content O(n^2)
    print(openedtabs)
    x=(input("please,enter the index of the tabs you want to display its content:"))
    if x.isdigit():
     index=int(x)
     if openedtabs[index] in openedtabs:   #searching for the index given by the user
        r=requests.get(openedtabs[index]['url'])      #send a request to get the content from the url, resources:youtube,w3schools,geeksforgeeks
        if (r.status_code==200):                      #checking if the request is accepted
         print(r.text)
     else :
        r=requests.get(openedtabs[len(openedtabs)-1]['url'])    
        if (r.status_code==200):
         print(r.text)
    else :
       print("please you have to give us the index as integer")
       Switch_Tabs()     

def Display_All_Tabs(openedtabs): #searching for title in openedtabs and displaying it,i didn't know how to figure out the nested titles O(n) 
    for i in openedtabs:
        print(i.get('title'))
          
def Open_Nested_Tabs(openedtabs):  #O(n^3)
    y=(input("please enter the index of the parent tab:"))
    if y.isdigit():
     index=int(y)  
     for index in openedtabs: #creating another dictionary in the index of the dictionary given by the user
        title=input("give us the title of the tab:")
        if title and title.isalnum():
            url=input("please enter the URL:")
            if url and url.startswith(("www.","http:","https:")):
                nestedtabs={"title":title,"url":url}
            else :
                url=input("please enter the url again:") 
        else :
            print("please input a valid Title!")
            Open_Nested_Tabs(openedtabs)  
    else :
       print("please give us the index as integer")
       Open_Nested_Tabs()                 

def Sort_All_Tabs(openedtabs):  #using selection method to sort the openedtabs alphabetically O(n^2)
    border=0
    while border<len(openedtabs)-1:
      minindex=border  #index of the minimum element
      for i in range (border+1,len(openedtabs)):  
        if openedtabs[i]['title']<openedtabs[minindex]['title']:
            minindex=i
      temp=openedtabs[border]  #swap the two elements
      openedtabs[border]=openedtabs[minindex]
      openedtabs[minindex]=temp
      border+=1
    print(openedtabs)        

def Save_Tabs(openedtabs): #O(1)
     file_path=input("enter the file path:")
     with open(file_path, 'w') as f:
         json.dump(openedtabs,f)     #just calling json to save the path given by the user
         print(f"saved path into {file_path}")

def Import_Tabs(openedtabs): #O(1)
    file_path=input("enter the file path:")
    with open(file_path) as p:
        read=json.load(p)   #loading the file
        print(read)         #printing the content
def mainmenu():
    choice=0
    while (choice!=9):     #O(n) n being the number of invalid values given by the user 
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
            Switch_Tabs() 
        elif (choice==4):
            Display_All_Tabs(openedtabs)
        elif(choice==5):
            Open_Nested_Tabs(openedtabs)
        elif(choice==6):
            Sort_All_Tabs(openedtabs)
        elif(choice==7):
            Save_Tabs(openedtabs)
        elif(choice==8):
            Import_Tabs(openedtabs)
        elif(choice==9):
            print("Bye Bye!")
        else :
            print("Please enter a valid number!")      
mainmenu()
