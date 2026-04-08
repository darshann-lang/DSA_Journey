class demo: 
    a = 4 # class attribute

o = demo()
print(o.a) # prints class attribute because instance attribute is not present
o.a = 0 # instanve attribute is set 
print(o.a) # prints instance attribute because instance is present
print(demo.a) # Prints the class attribute 