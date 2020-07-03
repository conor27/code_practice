# takes a word and returns true if last character is n, false if not

# optimal solution:
def is_last_character_n(word):
    return word.endswith("n")

# my solution (works):
def is_last_character_n(word):
	return word[-1] == "n"
