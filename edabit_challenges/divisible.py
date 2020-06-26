# takes an int and returns True if it's a factor of 100, False if not

# optimal solution
def divisible(num):
	return not num % 100

# ^this works bc in python False == 0

# my solution
def divisible(num):
	return (num % 100) == 0

