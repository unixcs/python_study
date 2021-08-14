"""
函数 调用 类
"""

class A(object):
    def __init__(self):
        self.name = "feng"
        print(self.name)

    @property
    def b(self):
        print(" i'm b")


def f():
    # A()
    a = A()
    a.b()


f()
