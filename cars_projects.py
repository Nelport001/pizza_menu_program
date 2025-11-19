cars = ['Ferrari', 'Audi', 'Porshe', 'Corvette']
# F STRINGS making a message with each element on the list
message = f"I my favorite car is {cars[2]}" 
print(message)
# Modifying an element on the list
cars[3] = 'Lamborghini Urus'
print(cars)
# .APPEND METHOD Add an element to the end of a list
cars.append('Pagani')
print(cars)
# .INSERT METHOD To insert an element anywhere in the list
cars.insert(0, 'Toyota')
print(cars)
# DEL STATEMENT Delete an element from a list
del cars[0]
print(cars)
popped_cars = cars.pop(2)
print(cars)
# .REMOVE METHOD this is to permanently remove an item from a list
cars.remove("Pagani")
print(cars)
# SORT() Function This is to permanently sort a lis in alphabetical order
cars.sort()
print(cars)
print(cars)
# SORTED() Funtion is to temporarily sort a list in alphabetical order.
print(sorted(cars))
print(cars)
# (reverse=True) Argument this is to reverse the order of a list.
cars.sort(reverse=True)
print(cars)
# REVERSE() Function this is to reverse the order of a list
cars.reverse()
print(cars)
# len() Function this is to find out the lenght of a list
print(len(cars))
print(cars)
