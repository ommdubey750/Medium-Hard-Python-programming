'''Write a program that asks user for a string s and a character c; and then prints out the location of each character c in the string s..'''
string=input("Enter the String : ")
character=input("Enter the Character : ")
length=len(string)
lst=[ ]
count=0
while count < length:
  position=string.find(character,count)
  lst.append(position)
  count+=1
lst=list(dict.fromkeys(lst))
lst_2=[]
for i in lst:
  if i==-1:
    continue
  lst_2.append(i)
print("Character a is found at locations : ",lst_2)
