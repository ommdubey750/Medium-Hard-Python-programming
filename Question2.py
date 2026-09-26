'''Write a program to input Principle, Rate of interest and Time. Calculate and display the Compound Interest.'''
principal=int(input("Enter the Principal : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the Time : "))
Amount=principal*(1+(rate/100))**time
cl=Amount-principal
print("Compound Interest : ",int(cl))