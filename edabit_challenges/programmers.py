# takes salaries of three programmers and returns biggest diff

# optimal solution:
def programmers(one, two, three):
    lst = [one, two, three]
    return (max(lst) - min(lst))

# my solution (works):
def programmers(one, two, three):
	nums = [one, two, three]
	nums.sort()
	return nums[2] - nums[0]

# had to tweak sorting line syntax
