class FirstClass(object):
    """docstring for FirstClass"""
    def setdata(self, value):
        """just set a value"""
        self.data = value
    def display(self):
        """just show the value"""
        print("data is {0}".format(self.data))

class SecondClass(FirstClass):
    """display it differently"""
    def display(self):
        """show with a different prefix"""
        print("this is different {0}".format(self.data))

class ThirdClass(SecondClass):
    """operator overloading"""
    def __init__(self, value):
        """constructor"""
        self.data = value

    def __add__(self, other):
        """ overload +"""
        return ThirdClass(self.data + other)

    def __str__(self):
        """overload for prints"""
        return "[ThirdClass value is {0}]".format(self.data)

    def mul(self, arg):
        """in place multiplier"""
        self.data *= arg


if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()
    z = SecondClass()
    th = ThirdClass("abc")
    x.setdata("King Arthur")
    y.setdata(3.142)
    z.setdata("new value")
    x.display()
    y.display()
    z.display()
    th.display()
    print(th)
    b = th + " added"
    print(b)
    th.mul(3)
    print(th)
    print(type(FirstClass))
