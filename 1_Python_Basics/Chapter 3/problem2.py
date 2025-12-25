# Write a program to fill in a letter template given below with name and date 
'''
letter = 
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''
letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Darshan").replace("<|Date|>","25 Dec 2025")) 
# here we've chained .replace() function to replace two words in a single variable 


''' or simply you can use: 
name = input("Enter your name: ")
date = input("Enter date: ")

print(f\'''  
            Dear {name},
            You are selected!
            {date}\''')
'''
