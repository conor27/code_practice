# takes a number, returns "even" or "odd"

# optimal solution:
def isEvenOrOdd(num):
    return 'odd' if num % 2 else 'even'

# alternative solution:
def isEvenOrOdd(num):
	return ["even", "odd"][num % 2]

# my solution (works):
def isEvenOrOdd(num):
	if num % 2:
		return "odd"
	else:
		return "even"
