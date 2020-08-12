class X(object):
    def __init__(self):
        super().__init__()
        self.x = "x"
class Y(object):
    def __init__(self):
        super().__init__()
        self.y = "y"
class Z(object):
    def __init__(self):
        super().__init__()
        self.z = "z"
class A(X, Y):
    def __init__(self):
        super().__init__()
        self.a = "a"
class B(Y, Z):
    def __init__(self):
        super().__init__()
        self.b = "b"
class M(A, B, Z):
    def __init__(self):
        super().__init__()
x = X()
y = Y()
z = Z()
a = A()
b = B()
m = M()
print("Attributes of x is", x.__dict__)
print("Attributes of y is", y.__dict__)
print("Attributes of z is", z.__dict__)
print("Attributes of a is", a.__dict__)
print("Attributes of b is", b.__dict__)
print("Attributes of m is", m.__dict__)
