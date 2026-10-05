'''Write a program to input a string and print number of upper- and lower- case letters in it.'''
st=input("Enter the String : ")
lower=0
upper=0
for i in st:
  if i.isupper():
    upper+=1
  elif i.islower():
    lower+=1
print("Number of upper-case letters : ",upper)
print("Number of lower-case letters : ",lower)
