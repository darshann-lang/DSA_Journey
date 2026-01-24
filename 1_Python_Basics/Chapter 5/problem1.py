# Write a program to create a dictonary of Hindi words with values as their english translation. Provide user with an option to look it up. 
words = {
    "kutta":"Dog",
    "billi":"cat",
    "chuha":"rat"
}

print("List: ")
for key in words:
    print(key)

word = input("Enter the word for translation: ")

print(words[word])