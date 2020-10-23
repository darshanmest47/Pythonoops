
# abstraction in python is the process of hiding the 
# implementation and exposing only required 
# functionality

from abc import ABC, abstractmethod
class A(ABC):
  def __init__(self):
    print('i am printing from master class A')

  @abstractmethod
  def operations(self):
    pass

  def print_simple(self):
    print('i am from A class and I am not abstract')

class B(A):
  def __init__(self,x,y):
    self.x =x
    self.y = y
    print('i am printing from B')

  def operations(self):
    print(self.x+self.y)


class C(A):
  def __init__(self,x,y):
    self.x =x
    self.y =y
    super ().__init__()

  def operations(self):
    print(self.x * self.y)


b =B(10,20)
c = C(20,20)

b.operations()
c.operations()
b.print_simple()
c.print_simple()
