"""
climbs the inhertance tree using namespace links
"""

def classtree(cls, indent):
    print('.' * indent, cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 2)

def instancetree(inst):
    print("Tree of {0}".format(inst))
    classtree(inst.__class__, 2)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass

    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()
