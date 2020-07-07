# takes customer age, and true or false if server is on break
# returns boolean whether or not drinks should be served
# customer must be at least 18, and server can't be on break.

# my solution/optimal (had to be corrected):
def should_serve_drinks(age, on_break):
	return age >= 18 and not on_break

# you forgot the not the first time, remember to think through the logic.
