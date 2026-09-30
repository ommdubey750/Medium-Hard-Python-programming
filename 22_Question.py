'''Write a program to sum the series : 1+1/2​+1/3​+1/4​+⋯+1/n'''
n=int(input("Enter the n'th Number : "))
sum=0
for i in range(1,n+1):
  fraction=1/i
  sum=sum+fraction
print(sum)
