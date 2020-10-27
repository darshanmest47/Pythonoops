class A:
  cls_var =2
  
  def one(self):
    print('one()')

  @classmethod
  def cls_mthd(cls):
    return cls.cls_var

  @staticmethod
  def st_mthd():
    print('static()')

class B(A):

  def two(self):
    print('two')

b =B()
b.one()
b.two()
print(b.cls_mthd())
b.st_mthd()

print(A.cls_mthd())
A.st_mthd()
 
#  one()
# two
# 2
# static()
# 2
# static()
