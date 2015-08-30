X = 11

def f():
    print(X)

def g():
   X = 22
   print(X)

class C(object):
    X = 33

    def m(self):
        X = 44
        self.X = 55

if __name__ == '__main__':
    print(X)
    f()
    g()

    obj = C()
    print(obj.X)

    obj.m()
    print(obj.X)
    print(C.X)

