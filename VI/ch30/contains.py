class Iters(object):
    """shows different methods of iteration"""
    def __init__(self, value):
        super(Iters, self).__init__()
        self.data = value

    def __getitem__(self, i):
        print("get[{0}]:".format(i), end='')
        return self.data[i]

    def __iter__(self):
        print("iter=>", end='')
        self.ix = 0
        return self

    def __next__(self):
        print("next:", end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print("contains:", end='')
        return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)

    for x in X:
        print(x, end='| ')

    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end='@')
        except StopIteration:
            break


