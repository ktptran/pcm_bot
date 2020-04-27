# Print out all the ingredients, their size and their measurement

recipe = {
    'ingredients': [
        {'id': 1, 'ingredient': 'flour', 'size': 200, 'measurement': 'mg'},
        {'id': 2, 'ingredient': 'eggs', 'size': 2, 'measurement': 'egg'},
        {'id': 3, 'ingredient': 'milk', 'size': 3, 'measurement': 'mL'}
    ]
}

# How do we get into the ingredients?
print(recipe['ingredients'][1]['ingredient'])

# How do we get the list of values in the list?
print(len(recipe['ingredients']))

# Now let's put it altogether and see2 if we can print
for val in range(len(recipe['ingredients'])):
#   print(f"{recipe['ingredients'][val]['ingredient']}: {recipe['ingredients'][val]['size']} + {recipe['ingredients'][val]['measurement']}")
    current = recipe['ingredients'][val]
    print(f'{current["ingredient"]}: {current["size"]} {current["measurement"]}')

# Final Solution
for val in range(len(recipe['ingredients'])):
    current = recipe['ingredients'][val]
    print(f'{current["ingredient"]}: {current["size"]} {current["measurement"]}')
