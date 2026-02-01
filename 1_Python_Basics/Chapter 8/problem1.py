# Write a program using functions to find the greatest of three numbers

def greatest():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if (a>b and a>c):
        g = a
    elif (b>c and b>a):
        g = b 
    elif (c>a and c>b):
        g = c
    
    print(f"Greatest number among three number is {g}")

greatest()