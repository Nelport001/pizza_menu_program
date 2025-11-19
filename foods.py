my_foods = ['pizza', 'falafel', 'carro cake']
friends_foods = my_foods[:]
for food in my_foods:
    print(f"{food.title()} is one of my favorite foods")
print("\n")
for food in friends_foods:
    print(f"{food.title()} is one of my friends favorite foods")