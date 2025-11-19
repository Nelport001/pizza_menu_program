# brother = {'first_name': 'Elkin', 'last_name': 'Portillo', 'age': 16, 'city': 'Fort Lauderdale'}
# print(brother['first_name'])
# print(brother['age'])
# brother_info = brother.get('city', 'Value not found')
# print(f"your brother lives in {brother_info}")
# favorite_numbers = {'aaron': 7,
#                     'daniel': 8,
#                     'elkin': 4,
#                     'Valentina': 9,
#                     'Kevin': 12}
# for key, number in favorite_numbers.items():
#     print(f"{key} favorite number is {number}")

person_1 = {'name': 'Nelson',
            'age': '24',
            'city': 'fort lauderdale'}
person_2 = {'name': 'elkin',
            'age': '16',
            'city': 'fort lauderdale'}
person_3 = {'name': 'aaron',
            'age': '22',
            'city': 'fort lauderdale'}
people = [person_1, person_2, person_3]
for person in people:
    print("\nperson's info:")
    for name, person_info in person.items():
        print(f"{name}:{person_info}")
         
      
