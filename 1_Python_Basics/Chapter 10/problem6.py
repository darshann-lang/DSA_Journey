class Calculator:
    def __init__(slf, n):
        slf.n =n

    def square(slf):
        print(f"The square is {slf.n* slf.n}")

    def cube(slf):
        print(f"The cube is {slf.n*slf.n*slf.n}")

    def squareroot(slf):
        print(f"The square root is {slf.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()