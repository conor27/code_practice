# returns true if b divides into a evenly, false if not

# most upvoted solution:
def divides_evenly(a, b):
	return a % b == 0

# my solution (works):
def divides_evenly(a, b):
	return not a % b
