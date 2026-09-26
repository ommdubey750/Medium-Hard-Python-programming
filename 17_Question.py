'''Write a Python program to print all Perfect numbers between 1 and 1000'''
start=int(input("Enter : "))
end=int(input("Enter : "))
print("Perfect Numbers : ")
for num in range(start,end+1):
  sum=0
  for i in range(1,num+1):
    if num%i==0:
      if i==num:
        continue
      sum=sum+i
  if num==sum:
    print(num)
