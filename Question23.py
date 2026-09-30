'''Write a program to sum the series: 1 + 1/2^2 + 1/3^2+ …..+ 1/4^2 + …..+ 1/n^2 '''
n=int(input("Enter the n'th Number : "))
sum=0
for i in range(1,n+1):
  power=i**2
  fraction=1/power
  sum=sum+fraction
print(sum)