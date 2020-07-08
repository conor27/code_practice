# see edabit for question breakdown
# takes number and returns number of boxes

# optimal solution:
def stack_boxes(n):
	return n ** 2

# my solution (works):
def stack_boxes(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		box_count = 1
		row_size = 1
		for item in range(n-1):
			row_size += 2
			box_count += row_size
		return box_count

# had to add -1 to the range, forgot about 0 index
