""" using yield in iter allows muliple iterators
    iterators"""
class SkipObject(object):
    def __init__(self, wrapped):
        super(SkipObject, self).__init__()
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item

if __name__ == '__main__':
    alpha = 'abcdefghijk'
    obj = SkipObject(alpha)
    i = iter(obj)
    print(next(i), next(i), next(i))

    for x in obj:
        for y in obj:
            print(x + y, end=' ')
