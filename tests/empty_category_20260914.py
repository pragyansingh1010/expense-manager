def safe_category(value):
    return value.strip() if value and value.strip() else 'Other'

assert safe_category('Food') == 'Food'
assert safe_category(' Travel ') == 'Travel'
assert safe_category('') == 'Other'
assert safe_category('   ') == 'Other'
print('Empty category rules passed')
