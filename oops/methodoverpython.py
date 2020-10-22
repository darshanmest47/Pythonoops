# method overloading python style

class Methodovpython:

    def results(self, num1=None, num2=None, num3=None, num4=None):
        if num1 != None and num2 != None and num3 != None and num4 != None:
            return num1 + num2 + num3 + num4
        elif num1 != None and num2 != None and num3 != None:
            return num1 + num2 + num3
        elif num1 != None and num2 != None:
            return num1 + num2
        else:
            print('requires atleast 2 args')


m = Methodovpython()

print(m.results(1,2,3))
