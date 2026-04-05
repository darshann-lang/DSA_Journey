with open("Chapter 9/first.txt") as f:
    content = f.read()

with open("Chapter 9/renamed_by_python.txt", "w") as f:
    f.write(content)