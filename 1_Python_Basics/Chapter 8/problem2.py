# Write a python program using function to convert celsius to fahrenheit
''' °C = (°F - 32) x 5/9'''

def ftoc(f):
    c = (f-32)*(5/9)    
    return c

f = int(input("Enter the fahrenheit :"))
print(f"Fahrenheit to Celsius is {round(ftoc(f), 2 )}")
