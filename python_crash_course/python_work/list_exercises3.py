# think of 5 places you'd like to visit and store them in a list

places_to_go = ['tokyo', 'san francisco', 'london', 'paris', 'barcelona']

print(places_to_go)

print(sorted(places_to_go))

print(places_to_go)

print(sorted(places_to_go, reverse=True))

print(places_to_go)

places_to_go.reverse()

print(places_to_go)

places_to_go.reverse()

print(places_to_go)

places_to_go.sort()

print(places_to_go)

places_to_go.sort(reverse=True)

print(places_to_go)
print()

# create a list and use all the operations on it

game_list = ['Pokemon', 'Skyrim', 'Runescape']

print(f"The best game ever is {game_list[0]}.\n")

print("There are lots of good games, in alpha order:")
print(sorted(game_list))
print()

print("In reverse alpha order:")
print(sorted(game_list, reverse=True))
print()

print(f"In this list, there are {len(game_list)} games.\n")

game_list.reverse()

print("From third to first:")
print(game_list)
print()

game_list.reverse()

print("And the other way again:")
print(game_list)
print()

game_list.sort()

print("And one last time alphabetically, this time using sort:")
print(game_list)

# intentionally tried to print game_list[3] to get an index error.