# create a variable called alien color and assign it either green, yellow, or
# red. write an if statement to test if it is green, try both pass and fail.

alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points!\n")

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points!")

# do it again but this time add an else

alien_color = "green"

# tried with green, now try running the else block

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points!\n")
else:
    print("You just earned 10 points!!\n")

# make another version with if-elif-else

# tried with all three colors

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points!\n")
elif alien_color == "yellow":
    print("You just earned 10 points!!\n")
else:
    print("You just earned 15 points!!!\n")


# Stages of life
# Create a program that determines a person's life stage based on their age

age = 67

if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")

print()

# Tested with all ages

favorite_fruits = ["watermelon", "blackberry", "raspberry"]

if "apple" in favorite_fruits:
    print("You like apple!")
if "watermelon" in favorite_fruits:
    print("You like watermelon!")
if "peach" in favorite_fruits:
    print("You like peach!")
if "blackberry" in favorite_fruits:
    print("You like blackberry!")
if "pear" in favorite_fruits:
    print("You like pear!")
