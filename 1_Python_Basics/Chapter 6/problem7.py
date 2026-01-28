# Write a program to find out whether a given post is talking about "Harry" or not

name = "Harry"

post = input("Enter your post: ")

if(name in post):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")