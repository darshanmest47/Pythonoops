class A:
    def one(self):
        print('one()')


class B(A):

    def two(self):
        print('two()')


b = B()

b.one()
b.two()
