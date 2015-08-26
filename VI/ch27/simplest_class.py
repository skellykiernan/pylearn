"""simplest class chapter 27
"""

def list_attrs(item):
    return [attr for attr in item.__dict__ if not attr.startswith('__')]


class rec: pass

rec.name = "Bob"
rec.age = 45
print(rec.name)

x = rec()
y = rec()
print(x.name, y.name)

x.name = "Sue"
print(rec.name, x.name, y.name)

print(list_attrs(rec))
print(list_attrs(x))
print(list_attrs(y))

def uppername(obj):
    """return name in uppercase"""
    return obj.name.upper()

rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))
