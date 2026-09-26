''' Write a Python program to print all Happy numbers between 1 and 1000'''
for num in range(1,20+1):
   n=num
   while n !=1 and n !=4:
     sum=0
     while n>0:
        digit=n%10
        sum=sum+digit**2
        n=n//10
     n=sum
   if n==1:
     print(num)
