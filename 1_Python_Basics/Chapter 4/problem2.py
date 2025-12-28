# Write a program to accept marks of 6 students and display them  in a sorted manner 

marks = []
print("Enter Marks for 6 students -- ")
m1 = int(input("Enter marks of student:" ))
marks.append(m1)
m2 = int(input("Enter marks of student:" ))
marks.append(m2)
m3 = int(input("Enter marks of student:" ))
marks.append(m3)
m4 = int(input("Enter marks of student:" ))
marks.append(m4)
m5 = int(input("Enter marks of student:" ))
marks.append(m5)
m6 = int(input("Enter marks of student:" ))
marks.append(m6)

marks.sort()
print(marks)