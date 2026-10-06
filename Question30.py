'''Write a program that reads a string and checks whether it is a palindrome or not without using string slice.'''
st=input("Enter the String : ")
length=len(st)
count=length-1
sum=" "
while 0 <= count:
  sum=sum+st[count]
  count-=1
if st in sum:
  print("This is palindrome ")
else:
  print("This is not a palindrome ")