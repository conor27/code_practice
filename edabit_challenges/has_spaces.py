# takes a string, returns true if it contains any spaces

# optimal solution:
def has_spaces(txt):
    return " " in txt

# my solution (works):
def has_spaces(txt):
	for letter in txt:
		if letter == " ":
			return True
	return False
