# encapsulation is the process of bundling the data
# and the methods in a single entity

class A:
  def __init__(self):
    self.__x = 20

  def get(self):
    print(f'Getting value....')
    print(f'Got value {self.__x}')

  def set(self,val):
    self.__x = val
    print(f'set value to {val}')

a = A()
a.get()
a.set(3000)
a.get()
