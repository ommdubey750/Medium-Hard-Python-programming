'''Write a Program that asks a user for a user-name and a code. Ensure that user doesn’t use their username as part of the code. Example: Enter user name: kobe Entercode : mykobeworld Your code should not contain your user name.'''
Username=input("Enter the User-name : ")
code=input("Enter the Code : ")
if Username in code:
  print("Invalid")
  print("Your code should not contain your user name.")
  print("Thankyou")
elif Username not in code:
  print("Valid")
  print("Thankyou")
