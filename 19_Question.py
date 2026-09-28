'''Write a program to enter a decimal number.Calculate and display the binary equivalent of it'''
num=int(input("Enter the Number : "))
binary=bin(num)
result=binary[2:]
print(result)
