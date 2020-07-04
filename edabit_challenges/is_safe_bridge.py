# takes a string, returns true if bridge is safe (no spaces), false if not

# optimal solution:
def is_safe_bridge(s):
	return " " not in s

# my solution (works):
def is_safe_bridge(s):
	return not " " in s
