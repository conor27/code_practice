# takes string, returns true if plural, false if not
# plurals end in letter 's'

# optimal solution
def is_plural(word):
    return word.endswith('s')

# my solution (works)
def is_plural(word):
	return word[-1] == "s"
