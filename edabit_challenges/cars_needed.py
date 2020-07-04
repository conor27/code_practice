# a car holds 1 driver and 4 passengers
# write a function that takes the number of people and returns number of cars

# optimal solution:
def cars_needed(n):
    return (n + 4) // 5

# my solution (works)
def cars_needed(n):
	cars = n // 5
	if n % 5:
		return cars + 1
	return cars
