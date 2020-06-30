# takes a first name and last name string
# return them in the format: lastname, firstname

# my solution / optimal (works):
def concat_name(first_name, last_name):
	return last_name + ", " + first_name

# alt solution
def concat_name(first_name, last_name):
	return "{0}, {1}".format(last_name, first_name)
