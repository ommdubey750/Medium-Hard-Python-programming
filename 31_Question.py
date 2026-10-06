''' Input a string having some digits. Write a program to calculate the sum of digits present in this string. ExEnter a string: k2i2it2 Sum of string’s digits is: 6'''
st=input("Enter the String : ")
sum=0
for i in st:
  if i.isdigit():
    integer=int(i)
    sum=sum+integer
print("Output : ",sum)
