'''Write a program to search an element in a given list.'''
List=[10,25,30,45,50]
search=int(input("Enter Search Element : "))
flag=0
for i in List:
  if i==search:
    flag+=1
if flag==1:
  print("Element Found ")
else:
  print("Element Not Found ")
