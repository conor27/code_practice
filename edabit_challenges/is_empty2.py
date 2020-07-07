# takes a dictionary. Returns true if it's empty false if not

# optimal solution:
def is_empty(dictionary):
    return not dictionary

# my solution (works, had to tweak)
def is_empty(dictionary):
	if dictionary:
		return False
	return True

# first time you mixed up the true and false, be careful with logic.
