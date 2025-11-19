favorite_numbers = {'Leon': [2, 3, 4],
                    'fanny': [5, 6],
                    'Ana': [8, 10, 16]}
for name, number in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for num in number:
        print(f"{num}")