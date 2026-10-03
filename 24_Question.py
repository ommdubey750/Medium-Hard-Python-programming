''' Write a program to input two strings. If strin1 is contained in string2, then create a third string with first four characters of strings, added with word “Restore”. Example: Enter String 1: rin Enter String 2: shagrin Output string: rin shagRestore.'''
st_1=input("Enter the first String 1 : ")
st_2=input("Enter the second String 2 : ")
restore="Restore"
if st_1 in st_2: 
  print("Yes Present")
  break_1=st_1[0:4]
  break_2=st_2[0:4]
  combine=break_1+break_2+restore
  print(combine)
else:
  print("Not Present Input Again")
