'''Write a program that reads a string and then prints a string that capitalizes every other letter in the string. Ex - passion becomes pAsSiOn'''
st=input("Enter the String : ")
length=len(st)
sum=" "
for i in range(length):
    if i%2!=0:
        capital=st[i].upper()
        sum=sum+capital
    else:
        sum=sum+st[i]
print(f"{st} become {sum} ")
