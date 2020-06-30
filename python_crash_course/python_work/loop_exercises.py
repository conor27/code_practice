# list_exercises

# make a list to store your three favourite types of pizza and print each one.

pizzas = ["deluxe", "canadian", "meat lovers"]

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nI back pizza big time!\n")

animals = ["dog", "cat", "fish"]

for animal in animals:
    print(f"It would be great to have a pet {animal}.")

print("\nThis animals are all popular pets.")

friend_pizzas = pizzas[:]

pizzas.append("cheese")

friend_pizzas.append("vegetarian")

print("\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

    