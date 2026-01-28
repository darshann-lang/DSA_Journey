# Write a program to calculate the grade of a student from his marks from the following scheme :
# 90 - 100 =>Ex
# 80 - 90 => A
# 70 - 80 => B
# 60 - 70 => C
# 50 - 60 => D
# <50 => F

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))

percentage = (100*(m1 + m2+ m3+ m4))/400

if (percentage<=100 and percentage >= 90):
    print("Grade: Ex")
elif (percentage<90 and percentage>=80 ):
    print("Grade: A")
elif (percentage<80 and percentage>=70 ):
    print("Grade: B")
elif (percentage<70 and percentage>=60 ):
    print("Grade: C")
elif (percentage<60 and percentage>=50 ):
    print("Grade: D")
else:
    print("Grade: F")

print("Percentage: ",percentage)