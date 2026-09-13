def valid_category(value):
    return isinstance(value, str) and bool(value.strip())

assert valid_category('Food')
assert valid_category(' Travel ')
assert not valid_category('')
assert not valid_category('   ')
print('Category rules passed')
