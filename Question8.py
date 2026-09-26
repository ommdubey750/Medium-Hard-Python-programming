'''Write a Python program to calculate the cumulative sum of numbers from 1 onwards. Stop the loop when the sum exceeds 50 using the break statement.  Output Current Sum = 1 Current Sum = 3 Current Sum = 6 ... Current Sum = 55'''
count=0
num=1
while num > 0:
    count=count+num
    print(f"Current Sum = {count}")
    num+=1
    if count>50:
        break