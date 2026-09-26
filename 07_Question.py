'''Write a Python program to print numbers from 1 to 50, skipping the numbers that are divisible by both 2 and 5 using the continue statement.'''
for num in range(1,50+1):
    if num%2==0 or num%5==0:
        continue
    print(num)
        
