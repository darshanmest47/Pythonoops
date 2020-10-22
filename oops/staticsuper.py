class A:
    val = 440
    def one(self):
        print('one()')

    def general(self):
        print('general')

    @staticmethod
    def one1():
        print('static()')
    @classmethod
    def cmethod(cls):
        return cls.val


class B(A):
    def two(self):
        print('two()')

    #calling using super

    def generalval(self):
        super().general()


b = B()

b.two()
b.one()
b.general()
# calling method containing super call
b.generalval()
# calling static
b.one1()
#class method
print(b.cmethod())


#o/p
# two()
# one()
# general
# general
# static()
# 440
