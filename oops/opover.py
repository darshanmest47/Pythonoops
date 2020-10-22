# operator overloading is said to be achieved if an operator performs an operation which is beyond it's normal operation
# here we are adding ,subtracting, and multiplying object datas


class A:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        m = self.x + other.y
        return m


class B:
    def __init__(self, y):
        self.y = y


class C:
    def __init__(self, z):
        self.z = z

    def __mul__(self, other):
        return self.z * other.z1


class D:
    def __init__(self, z1):
        self.z1 = z1


class First:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __sub__(self, other):
        m1 = self.num1 - other.num3
        m2 = self.num2 - other.num4

        return m1, m2


class Second:
    def __init__(self, num3, num4):
        self.num3 = num3
        self.num4 = num4


a = A(10)
b = B(20)

r = a + b  # (self.x,other.y)
print(r)

c = C(20)
d = D(30)

s = c * d  # (self.z,other.z1)
print(s)

f = First(20, 10)
se = Second(10, 5)

result = f - se
print(result)

# o/p
# 30
# 600
# (10, 5)
