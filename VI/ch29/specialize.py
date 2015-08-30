class Super(object):
    """Top class"""
    def method(self):
        """example method"""
        print("in Super.method")

    def delegate(self):
        """call a action if defined in subclass"""
        self.action()


class Inheritor(Super):
    """all methods in Super"""
    pass

class Replacer(Super):
    """Overrides Super.method"""
    def method(self):
        print("in Replacer.method")


class Extender(Super):
    """extend Super's Method"""
    def method(self):
        print("starting Extender.method")
        Super.method(self)
        print("ending Extender.method")

class Provider(Super):
    """provides an action for delegation"""
    def action(self):
        print("in Provider.action")


if __name__ == '__main__':
    for klass in (Super, Inheritor, Replacer, Extender):
        print(klass.__name__, "...")
        klass().method()
    print("Provider")
    x = Provider()
    x.delegate()
