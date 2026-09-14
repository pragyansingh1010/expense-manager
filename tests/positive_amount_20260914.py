def valid_amount(value):
    return isinstance(value, (int, float)) and value > 0

assert valid_amount(1)
assert valid_amount(99.99)
assert not valid_amount(0)
assert not valid_amount(-10)
print('Expense amount rules passed')
