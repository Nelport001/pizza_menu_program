pet_1 = {'breed': 'Pitbull',
         'owner': 'Raul'}
pet_2 = {'breed': 'German shepherd',
         'owner': 'Lucas'}
pet_3 = {'breed': 'Rottwailer',
         'owner': 'Juan'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print("\nPet's info:")
    for name, pet_info in pet.items():
        print(f"{name}:{pet_info}")