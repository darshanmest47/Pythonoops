# In duck typing no matter t which object the method belongs to as long as the method is present operaion is performed


class Ferrari:

    def brand(self):
        print('Ferrari')


class Lambourgeni:
    def brand(self):
        print('Lambourgeni')

class Jaguar:
    def speed(self):
        print('max-speed 400kmph')


def cars(obj):
    obj.brand()


f = Ferrari()
l = Lambourgeni()
j = Jaguar()


cars(f)
cars(l)
cars(j)

# as long as the method is present it is executed else error

# Traceback (most recent call last):
#   File "E:/pyoops/oops/ducktype.py", line 30, in <module>
#     cars(j)
#   File "E:/pyoops/oops/ducktype.py", line 20, in cars
#     obj.brand()
# AttributeError: 'Jaguar' object has no attribute 'brand'
# Ferrari
# Lambourgeni
