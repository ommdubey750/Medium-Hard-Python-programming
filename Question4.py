'''Write a program to solve a quadratic equation. The program should also take care if the roots are complex roots.'''
import cmath
num_1=int(input("Enter a : "))
num_2=int(input("Enter b : "))
num_3=int(input("Enter c : "))
Discriminant=(num_2**2)-4*num_1*num_3
if Discriminant < 0:
    root=cmath.sqrt(Discriminant)
    Cn_1=-(num_2)+root #Complex_number=(Cn)
    Cn_2=-(num_2)-root
    root_1=Cn_1/2
    root_2=Cn_2/2
    print("Root 1 : ",root_1)
    print("Root 2 : ",root_2)
    print("This is Complex Root ")
else:
    if Discriminant == 0:
        print("Same root ")
    else:
        root=Discriminant**0.5
        Cn=complex(0,root)
        Cn_1=-(num_2)+Cn
        Cn_2=-(num_2)-Cn
        root_1=Cn_1/2
        root_2=Cn_2/2
        print("Root 1 : ",root_1)
        print("Root 2 : ",root_2)
        print("This is real and Different root ")