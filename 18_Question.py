'''Write a program to read the numbers until-1 is encountered.Find the average of positive numbers and negative numbers entered by the user.'''
lst=[]
while True:
  num=int(input("Enter the Number : "))
  lst.append(num)
  if num==-1:
    break
count_1=0
count_2=0
positive=[ ]
negative=[ ]
for number in lst:
  if number > 0:
    count_1+=1
    positive.append(number)
  elif number < 0:
    if number==-1:
      continue
    count_2+=1
    negative.append(number)
sum_1=0
for avg_1 in positive:
  sum_1=sum_1+avg_1
average_1=sum_1/count_1
sum_2=0
for avg_2 in negative:
  sum_2=sum_2+avg_2
average_2=sum_2/count_2
print("Positive number average : ",average_1)
print("Negative number average : ",average_2)
