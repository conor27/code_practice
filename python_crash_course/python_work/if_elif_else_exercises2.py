# create a list of usernames, print a greeting for each,
# print a special greeting for admin.

usernames = ["helloword", "deadmau5", "bettycrocker", "admin", "jayz"]

if usernames:
	for name in usernames:
		if name == "admin":
			"Hello admin, would you like to see a status report?"
		else:
			print(f"Hey {name}! How's it going?")

else:
	print("We need to find some users!")

# make two lists, current users and new users. Loop through new users and make sure name's not
# taken. Print statement saying if it is or not. Make comparison case sensitive.

current_users = ["TylerTheCreator", "ChildishGambino", "ASAPRocky", "Superman", "Leonidas"]

new_users = ["Beavis", "TonyHawk", "Sum41", "tylerthecreator", "asapROCKY"]

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Oof sorry, you're going to have to pick a different name: that's taken")
	else:
		print(f"you're good to go {new_user}!")

print()
# print the correct ordinal number variation from 1-9 using loop and list:
number_list = [number for number in range(1,10)]

for number in number_list:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	elif number > 3:
		print(f"{number}th")


