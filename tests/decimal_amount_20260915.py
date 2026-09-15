def valid_amount(amount):
    return amount >= 0

assert valid_amount(10.50)
assert valid_amount(0.01)
assert not valid_amount(-0.01)
