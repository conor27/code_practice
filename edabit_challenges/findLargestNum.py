# takes a list and returns largest number. No negatives.

# best solution
def findLargestNum(nums):
	return max(nums)

# What I did:
def findLargestNum(nums):
	max_number = nums[0]
	for x in nums:
		if x > max_number:
			max_number = x
	return max_number
