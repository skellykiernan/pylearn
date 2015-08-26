class AttrDisplay(object):
    """Provides an inheritable display overload method that shows instances
       with their class names and a name=value pair for each attribute stored
       on the instance itself (but not attrs inherited from its classes). Can
       be any into any class, and will work on any instance."""

    def gatherAttrs(self):
        """get a list of the attrs"""
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        """format the attributes"""
        return '%s, %s' % (self.__class__.__name__, self.gatherAttrs())


def main():
    """adhoc testing"""
    class TopTest(AttrDisplay):
        """docstring for TopTest"""
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1

            TopTest.count += 2

    class SubTest(TopTest):
        """empty class for test with inheritance"""
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

if __name__ == '__main__':
    main()
