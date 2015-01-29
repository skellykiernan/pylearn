# Part A
L = ['a', 'b', 'c']
S = "string"
try:
    L + S
except TypeError as err:
    print('TypeError:', err)
T = (1,)
try:
    L + T
except TypeError as err:
    print('TypeError:', err)

# Part B
D = {'a':0}
try:
    L + D
except TypeError as err:
    print('TypeError:', err)


# Part C
# string has no append, does not make sense as string is immutable
# list, no problem appending

# Part D
# result type of concat
result = L + L
print(type(result), result)
result = S + S
print(type(result), result)
# result type of slicing
result = L[0:2]
print(type(result), result)
result = S[2:4]
print(type(result), result)
