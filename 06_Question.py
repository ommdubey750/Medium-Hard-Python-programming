'''Write a program to generate 3 random integers between 100 and 999 which is divisible by 5'''
Count=1
for num in range(100,1000):
    if Count < 4:
        if num%5==0:
            print(num)
            Count=Count+1
