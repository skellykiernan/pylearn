class Person(object):
    """from chapter 27"""
    def __init__(self, name, jobs, age=None):
        super(Person, self).__init__()
        self.name = name
        self.jobs = jobs
        self.age  = age

    def info(self):
        """get name and jobs for the person"""
        return (self.name, self.jobs)


def main():
    """as per book"""
    rec1 = Person("Bob", ["dev", "mgr"], 40.5)
    rec2 = Person("Sue", ["dev", "cto"])
    print(rec1.name, rec2.info())

if __name__ == '__main__':
    main()
