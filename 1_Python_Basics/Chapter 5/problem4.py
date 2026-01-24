# What will be the length of set s = (20, 20.00, '20') ?

s = set()
s.add(20)
s.add(20.00)
s.add('20')

print(s)
print("length of above set: ",len(s))

# In python the value is evaluated and determined if they are NUMERICALLY equal like : 1 == 1.0 will return true but 1 == "1" will return false 