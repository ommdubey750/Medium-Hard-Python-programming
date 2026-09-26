''' Write a Python program to print all prime numbers within a user-specified range.'''
start=int(input("Enter the Starting Number : "))
end=int(input("Enter the Ending Number : "))
for num in range(start,end+1):
  factors=0
  for i in range(1,num+1):
    if num%i==0:
      factors+=1
  if factors==2:
    print(num)