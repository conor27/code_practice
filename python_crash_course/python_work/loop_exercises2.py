# use a for loop to print the numbers from 1 to 20, inclusive

for number in range(1, 21):
    print(number)

# for number in range(1, 1_000_001):
    # print(number)


# print min, max, and sum of first million numbers
million_numbers = list(range(1,1_000_001))

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))
print("\n")

# print the odd numbers between 1 and 20 (inc)
for odd_number in range(1,21,2):
    print(odd_number)

# make a list of the multiples of 3 from 1 to 30
threes = list(range(3, 31, 3))

for three in threes:
    print(three)

# make a list with the cubed version of the first 10 numbers
cube_list = []
for number in range(1,11):
    cube_list.append(number**3)
print(cube_list)


# do the same thing but with list comprehension
cubes = list(cube ** 3 for cube in range(1, 11))

# print cube list
for cube in cubes:
    print(cube)

# prints the first three items in the list
print("\nThe first three items in this list are:")
print(cubes[:3])

print("\nThe three items in the middle of the list are:")
print(cubes[4:7])

print("\nThe three items at the end of the list are:")
print(cubes[-3:])

buffet_items = ("rice", "chicken", "pizza", "pasta", "chocolate")

print("\nThe buffet items are:")
for buffet_item in buffet_items:
    print(buffet_item.title())

# try to change tuple to see error:
# create new menu revising two items:
buffet_items = ("rice", "chicken", "pizza", "steak", "ice cream")

print("\nThe revised buffet items are:")
for buffet_item in buffet_items:
    print(buffet_item.title())

