# multiple inheritance
class A:

    def one(self):
        print('one')


class B:
    def two(self):
        print('two')


class C(A, B):

    def three(self):
        print('three()')


c = C()

c.three()
c.two()
c.one()

# o/p three()
# two
# one
