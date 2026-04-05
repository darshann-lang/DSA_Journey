word = "Donkey"

with open("Chapter 9/donkey.txt") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("Chapter 9/donkey.txt", "w") as f:
    f.write(contentNew)