# takes 3 arguements (probability of win, prize money, and cost to play) and returns
# True if gamble is profitable, and false if not. True if (prob * prize) > pay

# optimal solution
def profitable_gamble(prob, prize, pay):
	return prob * prize > pay

# how I did it
def profitable_gamble(prob, prize, pay):
	if (prob * prize) > pay:
		return True
	else:
		return False
