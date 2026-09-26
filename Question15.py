'''Write a Python program to print the first N prime numbers.'''
N=int(input(" Enter the N : "))
num=2
count=0
while count <N:
  factors=0
  for i in range(1,num+1):
    if num%i==0:
      factors+=1
  if factors==2:
    print(num)
    count+=1
  num+=1