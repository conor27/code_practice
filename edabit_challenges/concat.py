# takes two integer lists and returns a concatenated one

# best solution:
def concat(lst1, lst2):
	return lst1 + lst2

# alternative:
def concat(lst1, lst2):
	lst1.extend(lst2)
	return lst1

# my solution:
def concat(lst1, lst2):
	for x in lst2:
		lst1.append(x)
	return lst1
