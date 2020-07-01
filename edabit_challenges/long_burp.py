# takes int and return Burp with int number of R's

# optimal solution
def long_burp(num):
    return "Bu{}p".format("r" * num)

# my solution (works)
def long_burp(num):
	return "Bu" + "r"*num + "p"


