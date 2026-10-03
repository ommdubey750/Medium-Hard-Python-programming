'''Write a program to enter a number and then calculate its sum of digits.Also reverse the number.'''
num=int(input("Enter the Number : "))
temp=num
sum=0
reverse=0
while temp>0:
  digit=temp%10
  sum=sum+digit
  reverse=reverse*10+digit
  temp=temp//10
print("The Sum of digit : ",sum)
print("The reverse of digit : ",reverse)
