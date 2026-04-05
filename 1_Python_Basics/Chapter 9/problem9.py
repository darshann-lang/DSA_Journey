with open("Chapter 9/this.txt") as f:
    content1 = f.read()

with open("Chapter 9/this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("This Files are Identical")

else:
    print("Not Identical")