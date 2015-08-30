from person import Person
from manager import Manager

sue = Person("Sue Jones", job="dev", pay=100000)
bob = Person("Bob Smith")
tom = Manager('Tom Jones', 50000)

import shelve
with shelve.open('persondb') as db:
    for person in (sue, bob, tom):
        db[person.name] = person
    db.close()
