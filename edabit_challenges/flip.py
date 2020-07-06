# takes 1 and returns 0, or vice versa

# optimal solution:
def flip(y):
    return 1 - y

# my solution (works)
def flip(y):
	return int(not y)
