# Create an empty dictionary . Allow 4 friends to enter their fav language as value and use key as their names. Assume that the names are unique 
d = {}

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})

print(d)

# problem 7 -- if names of 2 friends are same; what will happen to the progranm in prob 6 ?
# Basically when two keys are same then the last assigned value will be considered. therefore the second value will be considered if two friends have same name 
# 
# problem 8 -- If languages of two friends are same ; what will happen to the program in prob 6?
#  different keys can have same values. 