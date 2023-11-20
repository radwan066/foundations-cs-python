def selectionSort(list1): 
 border=0
 while border <len(list1)-1:
  minIndex=border 
  for i in range(border+1, len(list1)):
    if list1[i].lower()< list1[minIndex].lower():
      minIndex=i
 
  temp=list1[border] 
  list1[border]=list1[minIndex]
  list1[minIndex]=temp

  border=border+1
 
 print(list1)

def sum(list1):
  sum=0
  for i in list1:
    sum+=i
  print(sum)  
list1=['aA', 'b', 'BD', 'Bc','D']
list2=[2,3,4,-5,6]
selectionSort(list1)
sum(list2)

