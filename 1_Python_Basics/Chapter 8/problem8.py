# Write a python function print a multiplication table of a given number 

def multab(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    
n = int(input("Enter a number: "))
multab(n)