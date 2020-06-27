# takes an int and returns true if it's divisible by 5, false if not

# optimal solution:
def divisible_by_five(n):
	return not n % 5

# my solution (works):
def divisible_by_five(n):
	return n % 5 == 0
