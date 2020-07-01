# write some predictions followed by checks for conditional statements

food = "taco"

print("Will food == 'taco' be True? Yes.")
print(food == "taco")

print("\nWill food == 'pizza' be True? Nope.")
print(food == "pizza")

food = "fries"

print("\nWill food == 'taco' be True? No.")
print(food == 'taco')

print("\nWill food == 'Fries' be True? No.")
print(food == 'Fries')

print("\nWill food == 'Fries'.lower()? be True Yes.")
print(food == 'Fries'.lower())

print("\nWill food != 'taco' be True? Yes.")
print(food != 'taco')

print("\nWill food != 'Taco' be True? Yep.")
print(food != 'Taco')

print("\nWill food != 'fries' be True? Nope.")
print(food != 'fries')

print("\nWill 5 <= 5 be True? Yup.")
print(5 <= 5)

print("\nWill 5 < 5 be True? Nope.")
print(5 < 5)

print("\nWill 600 > 500 be True? Yuup.")
print(600 > 500)

print("\nWill food == 'fries' and 5 < 7 be True? Definitely.")
print(food == "fries" and 5 < 7)

print("\nWill food == 'taco' or 7 > 5 be True? Yes.")
print(food == "taco" or 7 > 5)

food_list = ['taco', 'fries', 'pizza']

print("\nWill 'hamburger' be in food_list? False.")
print('hamburger' in food_list)

print("\nWill 'taco' be in food_list? Yeap.")
print('taco' in food_list)