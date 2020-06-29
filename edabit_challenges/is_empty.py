# takes string, returns true if empty, false if not

# my solution (works)
# remember to put variable on left side of comparative operator
def is_empty(test_string):
    return test_string == ""

# optimal solution:
def is_empty(test_string):
    return not test_string
