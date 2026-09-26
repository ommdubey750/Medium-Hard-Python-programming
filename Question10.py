''' Print all the even numbers from 1 to 50 and also display the sum of them.'''
count=0
for num in range(1,50+1):
    if num%2==0:
        print(num)
        count=count+num
print("Sum = ",count)