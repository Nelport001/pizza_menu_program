favorite_pizzas = ['Hawaiian', 'peperoni', 'bacon with meat']
friend_pizzas = favorite_pizzas[:]
# Try it yourself page 65
favorite_pizzas.append('cheese')
friend_pizzas.append('supreme')
for pizza in favorite_pizzas:
    print(f"I like {pizza.title()} pizza.")
print("I really love pizza!!")
for pizza in favorite_pizzas:
    print(f"My favorite pizzas are {pizza.title()}")
for pizza in friend_pizzas:
    print(f"My friend favorite pizzas are {pizza.title()}")

print("-")
for pizza in friend_pizzas:
    print(f"My friend likes {pizza.title()} pizza.")
print("He really loves pizza!!")
# Second Try it yourself of page 56
animals = ['shark', 'whale', 'dolphin']
for animal in animals:
    print(animal)
    [print(f"The {animal.title()} can swim fast")]
print("All this animals are from the ocean")