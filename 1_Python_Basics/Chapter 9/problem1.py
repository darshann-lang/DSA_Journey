f = open("Chapter 9/poem.txt")
content = f.read()

if ("twinkle" in content):
    print("twinkle is present in the content")
else:
    print("twinkle is not present in the content")

f.close()