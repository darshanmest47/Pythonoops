# In Python a method is said to be overloaded if it can perform multiple tasks
# General method overloading example (not supported in python)
class Methodover:

    def one(self,num1):
        print(num1)

    def one(self,num1,num2):
        print(num1,num2)

    def one(self,num1,num2,num3):
        print(num1,num2,num3)


mo = Methodover()

mo.one(2)

#o/p
# Traceback (most recent call last):
#   File "E:/pyoops/oops/methodoverloading.py", line 17, in <module>
#     mo.one(2)
# TypeError: one() missing 2 required positional arguments: 'num2' and 'num3'
