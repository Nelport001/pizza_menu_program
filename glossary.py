glossary = {'for': 'To loop through data',
            'while': 'To loop through a program infinetely',
            'insert()': 'to insert data in a list or dictionary',
            'list': 'Used to store data inside of them',
            'remove()': 'To remove data from aa list'}
for word, definition in glossary.items():
    print(f"{word.title()}: {definition.title()}")
glossary['sort()'] = 'Used to sort the items of a list in alphabetical order'
glossary['True'] = 'A conditional test to check if a condition is met'
glossary['False'] = 'A condition test to  check if a condition is not met'
glossary['sorted()'] = 'To sort a list in alphabetical order but just once'
glossary['if'] = 'is a conditional statement to check if something is true or false'
for word, definition in glossary.items():
    print(f"{word.title()}: {definition.title()}")

