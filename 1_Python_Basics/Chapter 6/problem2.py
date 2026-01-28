# Write a program to find out whether a student has passsed or failed if it requires a total of 40% & atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

percentage = (100*(m1 + m2 + m3))/300 

if (percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass!:",percentage)
else:
    print("You are fail!",percentage)