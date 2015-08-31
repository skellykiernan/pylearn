""" separating iterator and object holding data allows to have multiple
    iterators"""
class SkipObject(object):
    def __init__(self, wrapped):
        super(SkipObject, self).__init__()
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator(object):
    def __init__(self, wrapped):
        super(SkipIterator, self).__init__()
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset > len(self.wrapped):
            raise StopIteration
        item = self.wrapped[self.offset]
        self.offset += 2
        return item

if __name__ == '__main__':
    alpha = 'abcdefghijk'
    obj = SkipObject(alpha)
    i = iter(obj)
    print(next(i), next(i), next(i))

    for x in obj:
        for y in obj:
            print(x + y, end=' ')
