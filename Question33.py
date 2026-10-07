'''Write a program that inputs a string that contains a decimal number and prints out the decimal part of the number. For example, if the number is 515.8059, the program should print 8059.  (Do by partition function'''
st=input("Enter the Decimal Number String : ")
parts=st.partition(".")
print(parts[2])