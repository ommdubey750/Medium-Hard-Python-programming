'''Write a program to find the sum of squares of even numbers upto n.'''
n=int(input("Enter the n(th) : "))
sum=0
for i in range(n+1):
  if i%2==0:
    even=i**2
    sum=sum+even
print("Sum of squares of even numbers = ",sum)
