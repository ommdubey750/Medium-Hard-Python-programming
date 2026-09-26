''' Write a Python program to check whether a number is a happy number.'''
num=int(input("Enter the number : "))
sum=0
while sum !=1:
   if num==0:
      num=sum
      sum = 0
   while num>0:
     digit=num%10
     num=num//10
     power=digit**2
     sum=sum+power
if sum==1:
   print("Happy Number : ")
