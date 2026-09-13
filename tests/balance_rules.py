def balance(income, expenses):
    return income - expenses

assert balance(1000, 400) == 600
assert balance(500, 500) == 0
assert balance(200, 300) == -100
print('Expense balance rules passed')
