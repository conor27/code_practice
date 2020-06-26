# takes a string an an integer and returns the string repeated that number of times
# ex. repetition("cherry", 2) -> "cherrycherry"

def repetition(txt, n):
	return '' if not n else txt + repetition(txt, n-1)

# OR

def repetition(txt, n):
	return  txt*n

