class A:

    def __init__(self):
        self.name = 'Darshan'
        print('Darshan')

    def one(self):
        print('one()')


class B:
    def __init__(self):
        self.salary = 20000
        print('20000')

    def two(self):
        print('two()')


class C(A, B):

    def __init__(self):
        super().__init__()

    def three(self):
        print('three()')
        print(self.name)


# if a single class inherits from multiple classes and if parent classes have constructors
# values then Method resoultion order will be executed from left to right

class D(B, A):
    def __init__(self):
        super().__init__()

    def four(self):
        print('four()')
        print(self.salary)


c = C()
c.three()
c.one()
c.two()

print()
d = D()
d.one()
d.two()
d.four()


#o/p
# Darshan
# three()
# Darshan
# one()
# two()
#
# 20000
# one()
# two()
# four()
# 20000
#
# Process finished with exit code 0
