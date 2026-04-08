class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Darshan", 1200000, 12345)
print(p.name, p.salary, p.pincode, p.company)

r = Programmer("Dev", 1000000, 54321)
print(r.name, r.salary, r.pincode, r.company)