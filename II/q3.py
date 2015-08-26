L = ['a', 'b', 'c', 'd']
# assign an empty list to L[2] inserts the empty list
L[2] = []
print(L)
# assign an empty list to a slice L[2:4],
# removes the indices specified by the list
# Note: can be single or multiple indices
L[2:4] = []
print(L)

# restore the list getting two small
L = ['a', 'b', 'c', 'd']
# use 'del' to remove from list ( odd that del is not a function syntax !!!!)
del L[2]
print(L)
# use 'del' to remove a slice from the list
del L[0:2]
print(L)
# assign a mon-sequence to a slice, Will give a TypeError as not iterable
L = ['a', 'b', 'c', 'd']
try:
    L[2:3] = 1
    print(L)
except TypeError as err:
    print('TypeError', err)

