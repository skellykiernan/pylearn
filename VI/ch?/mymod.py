def countLines(name):
    """count number lines in a file"""
    with open(name, 'r') as fd:
        num_lines = len(fd.readlines())
    return num_lines


def countChars(name):
    """count number characters in a file"""
    with open(name, 'r') as fd:
        num_chars = len(fd.read())
    return num_chars


def test(name):
    """test both functions"""
    num_lines = countLines(name)
    num_chars = countChars(name)
    print("%s has %d lines and %d chars" %
            (name, num_lines, num_chars))

if __name__ == '__main__':
    test('mymod.py')
