from person import Person


class Manager(Person):
    """A manager person"""

    def __init__(self, name, pay):
        """constructor"""
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        """of course different for managers"""
        Person.giveRaise(self, percent + bonus)


def main():
    """adhoc testing"""
    sue = Person("Sue Jones", job="dev", pay=100000)
    bob = Person("Bob Smith")
    sue.giveRaise(.10)
    tom = Manager('Tom Jones', 50000)
    print(tom)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

    for person in (bob, sue, tom):
        person.giveRaise(.10)
        print(person)


if __name__ == '__main__':
    main()
