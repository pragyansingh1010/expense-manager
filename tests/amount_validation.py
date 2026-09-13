def valid_amount(value):
    return isinstance(value, (int, float)) and value >= 0

assert valid_amount(0)
assert valid_amount(125.50)
assert not valid_amount(-1)
assert not valid_amount('125')
print("Expense amount validation tests passed")
