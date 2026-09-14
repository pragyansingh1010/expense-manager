def valid_amount(value):
    return value > 0

assert not valid_amount(0)
assert valid_amount(0.01)
assert not valid_amount(-0.01)
print('Zero expense amount rule passed')
