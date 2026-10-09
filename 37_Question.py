''' Write a program to find the mean of the given list of numbers. Take the numbers from the user during run time.'''
numbers = list(map(int, input("Enter the numbers : ").split()))
length=len(numbers)
sum=0
for i in numbers:
  sum=sum+i
mean=sum/length
print("Mean = ",mean)
