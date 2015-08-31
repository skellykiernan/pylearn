class Squares(object):
    """iterator that returns square if vakues in the specified range"""
    def __init__(self, start, stop):
        super(Squares, self).__init__()
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

if __name__ == '__main__':
    for i in Squares(1, 6):
        print(i, end=' ')
    l = list(Squares(1, 6))
    print(l)

    # Only a sinle iteration
    X = Squares(3, 7)
    print(tuple(X), tuple(X))
