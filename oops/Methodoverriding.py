# Method overriding


class A:

    def one(self):
        print('one()')


class B(A):
    def one(self):
        print('two()')


b = B()

b.one()

# o/p
# two()
# 1
