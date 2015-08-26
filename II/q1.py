#! /usr/bin/env python3
# Bulk of these are intended for the console, so added a lot of prints

print(' ---- Q1')
print(2 ** 16)

print('-- division always returns float, python2 difference')
print((2 / 5, 2 / 5.0))

print('-- shows various string concatenation')
print("spam" + "eggs")
S = "ham"
print("eggs " + S)

print('-- shows string repeat')
print(S * 5)
print('-- slice to produce empty string')
print(S[:0] is '')
print('-- two styles of string formatting')
print("green %s and %s" % ("eggs", S))
print('green {0} and {1}'.format('eggs', S))

print('-- tuples')
# single element tuple needs the coma to distinguish it from arithmetic values
print(('x',)[0])
print(('x', 'y')[1])

print('-- Lists')
L = [1, 2, 3] + [4, 5, 6]
print(L)
print(L[:], end=''); print(' L[:] give a new list %s' % (L is not L[:]))
print(L[:0], end=''); print(' L[:0] give a empty list %s' % (L[:0] == []))
print(L[-2], end=''); print(' L[-2] is indexing two from end')
print(L[-2:], end=''); print(' L[-2:] is slices the last two')
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])
L.reverse(); print('L.reverse() = ', L)
L.sort(); print('L.sort() = ', L)
L.index(4); print('L.index(4) = %d , gives the index number occurs at' % (L.index(4),))

print('-- dictionaries')
print("{'a': 1, 'b': 2}['b'] =",{'a': 1, 'b': 2}['b'])
D = {'x': 1, 'y': 2, 'z': 3}; print('dict D =', D)
D['w'] = 0; print('dict D =', D)
print("D['x'] + D['w'] =", D['x'] + D['w'])
print('- tuple as a key')
D[(1, 2, 3)] = 4; print('dict D =', D)
print('list(D.keys()) =', list(D.keys()))
print('list(D.values()) =', list(D.values()))
print('(1, 2, 3) in D = ',(1, 2, 3) in D)

print('-- Create Lists with empties')
print('[[]] = ', [[]])
print('["", [], (), {}, None] = ',["", [], (), {}, None])
