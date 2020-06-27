# return true if K^K = N, false if not

# optimal solution:
def k_to_k(n, k):
	return n == k ** k

# my solution: works
def k_to_k(n, k):
	return (k**k==n)
