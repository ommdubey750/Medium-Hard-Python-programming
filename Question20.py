'''Write a program that prompts users to enter numbers.The process will repeat until user enters-1.Finally,the program prints the count of prime and composite numbers entered.'''
lst=[ ]
prime=[ ]
composite=[ ]
while True:
  num=int(input("Enter the Number : "))
  lst.append(num)
  if num==-1:
    break
for x in lst:
  count=0
  if x==-1:
    continue
  for y in range(1,x+1):
    if x%y==0:
      count+=1
  if count==2:
    prime.append(x)
  else:
    composite.append(x)
length_prime=len(prime)
length_composite=len(composite)
print("Total Prime Number : ",length_prime)
print("Total Composite Number : ",length_composite)