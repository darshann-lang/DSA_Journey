# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect this spam 

p1 = "Make a lot of money"
p2 = "Click this"
p3 = "Subscribe this"
p4 = "Buy now"

msg = input("Enter your comment: ")

if ((p1 in msg) or (p2 in msg) or (p3 in msg) or(p4 in msg)):
    print("SPAM DETECTED")

else:
    print("Not a spam")