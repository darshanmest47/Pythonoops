# multilevel inheritance

class A:

    def one(self):
        print('one()')

class B(A):

    def two(self):
        print('two()')

class C(B):

    def three(self):
        print('three()')


c= C()

c.one()
c.two()
c.three()