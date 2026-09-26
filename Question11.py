''' Write a Python program to print the numbers from 1 to 30, skipping all multiples of 3 using the continue statement.'''
for num in range(1,30+1):
    if num%3==0:
        continue
    print(num)
    