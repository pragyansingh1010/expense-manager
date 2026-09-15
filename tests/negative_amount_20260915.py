def valid_amount(amount):
    return amount >= 0

assert valid_amount(0)
assert valid_amount(25)
assert not valid_amount(-1)
