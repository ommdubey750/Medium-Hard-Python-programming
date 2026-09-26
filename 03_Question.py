'''Write a program to accept name and age — check if the user is a valid voter (18+).
Example: Input: Shery, 20
Output: Hello Shery, you are a valid voter'''
name=input("Enter your name : ")
age=int(input("Enter your age : "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print("I am Sorry you are not valid voter ")
