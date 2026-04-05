words = ["Donkey", "animals"]

with open("Chapter 9/donkey.txt") as f:
    content = f.read()

for word in words:
    contentNew = content.replace(word, "#"* len(word))

with open("Chapter 9/donkey.txt", "w") as f:
    f.write(contentNew)