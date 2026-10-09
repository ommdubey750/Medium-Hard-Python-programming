'''Write a program to count the frequency of a given element in a list of numbers.'''
List=[10,20,10,30,10,40,20]
element=int(input("Enter the Element : "))
count=0
for i in List:
  if i==element:
    count+=1
print(f"The frequency of {element} = {count} ")