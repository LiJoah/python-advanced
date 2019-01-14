class A(object):
    # 类变量
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)

# A.aa = 11
# a.aa = 100
# 先在 self 中寻找， 然后在 A 类对象中寻找
print(a.x, a.y, a.aa)
print(A.aa)
# 这里是获取的是实例的属性对象
print(a.__dict__)
# 这里是获取的是类对象的属性对象
print(A.__dict__)

b = A(3,5)
print(b.aa)