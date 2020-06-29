# given a list return difference between biggest and smallest num

# optimal solution:
def difference(nums):
	nums.sort()
	return nums[-1] - nums[0]

# my solution (works):
def difference(nums):
	return max(nums) - min(nums)
