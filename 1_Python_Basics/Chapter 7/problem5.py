# Write a program to find the sum of first n natural numbers using WHILE loop
n = int(input("Enter a number: "))

i = 0
sum = 0
while i<=n:
    sum +=i
    i+=1
print(sum)