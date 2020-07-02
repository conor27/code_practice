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

alien_color = "yellow"

if alien_color == "green":
	print("You just earned 5 points!\n")
elif alien_color == "yellow":
	print("You just earned 10 points!!\n")
else:
	print("You just earned 15 points!!!\n")

