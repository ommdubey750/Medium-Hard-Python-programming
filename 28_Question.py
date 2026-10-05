'''Write a program that asks the user for a string and creates a new string that doubles each character of the original string. Example: Enter a string: sipo Doubled string: ssiippoo'''
st=input("Enter the String : ")
sum=" "
for i in st:
  Doubled=i*2
  sum=sum+Doubled
print("Doubled String : ",sum)
