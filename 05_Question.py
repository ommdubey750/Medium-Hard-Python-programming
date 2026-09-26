'''Write a program that asks a user for a number of years, and then prints out the number of days, hours, minutes and seconds in the number of years.
Example-
How many years? 10
10.0 years is:
3650.0 days
87600.0 hours
5256000.0 minutes
315360000.0 seconds'''
years=int(input("Enter the years : "))
Days=years*365
Hours=Days*24
Minutes=Hours*60
Seconds=Minutes*60
print(f" {years} Years is : ")
print(f"{Days} Days ")
print(f"{Hours} Hours ")
print(f"{Minutes} Minutes ")
print(f"{Seconds} Seconds ")
