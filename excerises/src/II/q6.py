D = {'a': 0, 'b': 1, 'c': 2}
# Attempting to access a key that does not exist
# will result in a KeyError Exception
try:
    D['d']
except KeyError as err:
    print('KeyError for', err)
# Assign to a non-existing key (will create entry)
D['d'] = 'spam'
print(D)
# For Lists cannot assign to a non-existing index
L = ['a', 'b', 'c']
try:
    L[3] = 'd'
except IndexError as err:
    print('IndexError ', err)