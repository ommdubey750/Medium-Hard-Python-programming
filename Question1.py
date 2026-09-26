'''Write a program to create an Income Tax Calculator, where you calculate the tax.
Calculate tax based on the following slabs:
- Income ≤ ₹2,50,000 → No Tax
- ₹2,50,001 – ₹5,00,000 → 5%
- ₹5,00,001 – ₹10,00,000 → 20%
- Above ₹10,00,000 → 30%'''
Income=int(input("Enter the Income : "))
if Income <= 250000:
    print("No Tax")
elif 250001 >= Income or Income <= 500000:
    slab_1=Income-250000
    tax=slab_1*(5/100)
    print("Tax : ",tax)
elif 500001 >= Income or Income <= 1000000:
    slab_2=500000-250000
    tax_1=slab_2*(5/100)
    slab_3=Income-500000
    tax_2=slab_3*(20/100)
    cal=tax_1+tax_2
    print("Tax : ",cal)
else:
    slab_2=500000-250000
    tax_1=slab_2*(5/100)
    slab_3=1000000-500000
    tax_2=slab_3*(20/100)
    slab_4=Income-1000000
    tax_3=slab_4*(30/100)
    cal=tax_1+tax_2+tax_3
    print("Tax : ",cal)