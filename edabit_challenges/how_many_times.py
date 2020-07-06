# takes int, returns Edabit with int number of a's

# optimal solution:
def how_many_times(num):
    return "Ed{}bit".format("a"*num)

# my solution (works):
def how_many_times(num):
	return "Ed" + "a"*num + "bit"
