# takes a list and returns sum

# optimal solution
get_sum_of_elements=sum

# alternate
def get_sum_of_elements2(lst):
    return sum(lst)

# my corrected solution
def get_sum_of_elements3(lst):
	sum = 0
	if len(lst) > 0:
		for x in lst:
			sum += x
		return sum
	else:
		return ''

print(get_sum_of_elements([1,2,3]))
