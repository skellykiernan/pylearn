from classtools import AttrDisplay

class Person(AttrDisplay):
    """record for a person"""
    def __init__(self, name, job=None, pay=0):
        super(Person, self).__init__()
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        """get last name"""
        return self.name.split()[-1]

    def giveRaise(self, percent):
        """bump pay"""
        self.pay = int(self.pay * (1 + percent))

#    def __repr__(self):
#        """special repr"""
#        return '[Person: {0}, {1}]'.format(self.name, self.pay)


def main():
    """adhoc testing"""
    sue = Person("Sue Jones", job="dev", pay=100000)
    bob = Person("Bob Smith")
    print(sue)
    print(bob)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

if __name__ == '__main__':
    main()
