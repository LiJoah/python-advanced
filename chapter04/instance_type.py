class A:
    pass

class B(A):
    pass

b = B()

# isinstance 这个函数检测只能检测到继承关系， 不能检测直接继承关系
print(isinstance(b, B)) # true
#
print(isinstance(b, A)) # true

print(isinstance(b, A)) # true
