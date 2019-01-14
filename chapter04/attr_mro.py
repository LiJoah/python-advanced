#新式类

class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass

# 这里是 python3 的多继承
#A -> B -> D -> C -> E
print(A.__mro__)