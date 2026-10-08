''' Write a program that inputs a line of text and prints its each word in a separate line. Also, print the number of words in the line. (Use split function) Example: Enter a line : Python is fun. Python is fun. Total words: 3'''
st=input("Enter the line : ")
result=st.split()
count=0
for i in result:
  count+=1
print("Total Words : ",count)