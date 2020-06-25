# takes a list and returns a dictionary with each (key, value) pair being
# the letter (lower case, upper case) respectively

def mapping(letters):
	return {i:i.upper() for i in letters}

# alternative:
def mapping(letters):
	dict = {}
	for letter in letters:
		dict[letter.lower()] = letter.upper()
	return dict

# my solution:
def mapping(letters):
	pair_list = {}
	for x in letters:
		pair_list.update({x.lower():x.upper()})
	return pair_list



# notes: forgot the {} within update() brackets first time around
