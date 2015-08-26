from person import Person
from manager import Manager


class Department(object):
    """as in work"""
    def __init__(self, *people):
        super(Department, self).__init__()
        self.members = list(people)

    def addMember(self, person):
        """new person after construction"""
        self.members.append(person)

    def giveRaises(self, percent):
        """when all get the same raise"""
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        """display all department members"""
        for person in self.members:
            print(person)


def main():
    """adhoc testing"""
    sue = Person("Sue Jones", job="dev", pay=100000)
    bob = Person("Bob Smith")
    tom = Manager('Tom Jones', 50000)
    dep = Department(sue, bob)
    dep.showAll()
    dep.addMember(tom)
    dep.showAll()
    dep.giveRaises(.10)
    dep.showAll()


if __name__ == '__main__':
    main()
