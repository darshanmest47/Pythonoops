class A:
  def __init__(self):
    print('from A')
  def say_hi(self):
    print('sayhi from A')

class B:
  def __init__(self):
    print('from B')
  def say_hi(self):
    print('sayhi from B')

class C(B,A):
  def say_hi(self):
    print('sayhi from C')

c = C()
c.say_hi()


# from B
# sayhi from C
# if the inheritance is multiple
# and if there is constructor in parent class
# then method resolution order is executed
