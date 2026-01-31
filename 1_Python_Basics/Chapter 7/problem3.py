# Write a program to print multiplication table of a given number using WHILE loop 

i = 1
n = int(input("Enter a number: "))

while i<=10:
    print(f"{n} x {i} = {n*i}")
    i +=1
    