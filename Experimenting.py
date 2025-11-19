# drive = input("Do you know how to drive?:")
# legal_age_alcohol_and_drive = input("what is your age to drink?:")



# if legal_age_alcohol_and_drive <= "21" and drive >= "yes" and legal_age_alcohol_and_drive >= "16":
#     print("You are not old enough to drink but at least you can drive")
# else:
#     print("sorry you are not old enough to drink neither drive")

# age = input("What is your age?:")
# if age < "4":
#     price = 0  
# else:
#     price = 45
# print(f"Your admission price is ${price}")
# import time

# requested_toppings = input("What do you want to add to your pizza?:")
# if requested_toppings == 'green peppers':
#     print("Sorry We dont add that crap")
# elif requested_toppings.lower() == 'onions':
#     print("Sorry We dont add that crap")
# else:
#     print(f"Adding {requested_toppings} to your  pizza!")
# while True:
#     requested_toppings_2 = input("What else do you want to add to your pizza? (Type 'done' to finish):")
#     if requested_toppings_2 == 'done':
#         print("Okay perfect. Your pizza will be ready in 5 seconds!")
#         break
#     elif requested_toppings_2.lower() == 'onion':
#         print("Sorry We dont add that crap")
#     elif requested_toppings_2.lower() == 'green peppers':
#         print("Sorry We dont add that crap")
#     else:
#         print(f"Adding {requested_toppings_2} to your  pizza!")
# for i in range(5, 0, -1):
#     print(f"{i}....")
#     time.sleep(1) #waits one second
# print("Your Pizza is ready! Enjoy!")

# cars = ['toyota', 'Subaru']
# print(cars)
# cars.reverse()
# print(cars)
# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#     print(new_alien)
# alien_color = new_alien.get('color')
# print(alien_color)
favorite_colors = {'aaron': ['red', 'blue', 'yellow'],
                   'elkin': ['purple', 'black'],
                   'danubia': ['pink', 'orange']}
for name, colors in favorite_colors.items():
    print(f"{name.title()} favorite color is:")
    for color in colors:
        print(f"\t{color}")
