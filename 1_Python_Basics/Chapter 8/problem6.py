# Write a python function which converts inches to cm 
''' cm = inches x 2.54'''

def inchtocm(cm):
    cm = inches * 2.54
    return cm 

inches = int(input("Enter the inches: "))
print(f"Inches to Centimeter is {round(inchtocm(inches), 2)} cm ")