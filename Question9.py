'''Write a Python program to print numbers from 1 to 50. Stop the loop when the first multiple of 7 greater than 20 is encountered. Output 1 2 3 ... 20 21'''
for num_1 in range(1,10+1):
    Multiple=7*num_1
    if Multiple > 20:
        break
for num_2 in range(1,Multiple+1):
    print(num_2)