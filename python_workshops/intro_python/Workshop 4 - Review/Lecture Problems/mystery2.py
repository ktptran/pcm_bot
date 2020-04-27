# Rename the key size to amount for any dictionary of the same style

recipe = {
    'ingredients': [
        {'id': 1, 'ingredient': 'flour', 'size': 200, 'measurement': 'mg'},
        {'id': 2, 'ingredient': 'eggs', 'size': 2, 'measurement': 'egg'},
        {'id': 3, 'ingredient': 'milk', 'size': 3, 'measurement': 'mL'}
    ]
}

# How do we get to the measurement value?
print(recipe['ingredients'][1]['measurement'])

# How do we reassign a value
# recipe['ingredients'][1]['amount'] = recipe['ingredients'][1].pop('size')
print(recipe['ingredients'][1])

# How do we get the length of the list?
print(len(recipe['ingredients']))

# How do we reassign the values for all of them in this dictionary?
# length = len(recipe['ingredients'])
# for val in range(length):
#    recipe['ingredients'][val]['amount'] = recipe['ingredients'][val].pop('size')

# print(recipe['ingredients'])

# How can we make this work for any type?
def rewrite(recipe):
    length = len(recipe['ingredients'])
    for val in range(length):
        recipe['ingredients'][val]['amount'] = recipe['ingredients'][val].pop('size')
    print(recipe['ingredients'])

rewrite(recipe)
