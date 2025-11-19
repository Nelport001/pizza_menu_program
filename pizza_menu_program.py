import time
pizza_toppings = []
requested_toppings = input("What do you want to add to your pizza?:")
if requested_toppings == 'green peppers':
    print("Sorry We dont add that crap")
elif requested_toppings.lower() == 'onions':
    print("Sorry We dont add that crap")
else:
    print(f"Adding {requested_toppings} to your  pizza!")
    pizza_toppings.append(requested_toppings)
    print(f"chosen toppings {pizza_toppings}")
while True:
    requested_toppings_2 = input("What else do you want to add to your pizza? (Type 'done' to finish):")
    if requested_toppings_2 == 'done':
        confirm = input(f"This are your chosen toppings {pizza_toppings} to comfirm type 'Yes' or 'No':")
        if confirm.lower() == 'yes':
            print("Perfect your pizza will be ready in 5 seconds")
            break
    elif requested_toppings_2.lower() == 'onion':
        print("Sorry We dont add that crap")
    elif requested_toppings_2.lower() == 'green peppers':
        print("Sorry We dont add that crap")
    else:
        print(f"Adding {requested_toppings_2} to your  pizza!")
        pizza_toppings.append(requested_toppings_2)
        print(f"chosen toppings {pizza_toppings}" )
    
for i in range(5, 0, -1):
    print(f"{i}....")
    time.sleep(1) #waits one second
print("Your Pizza is ready! Enjoy!")