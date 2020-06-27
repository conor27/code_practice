# takes a name, and return "Hello *name*!"

# optimal solution:
def hello_name(name):
    return "Hello {}!".format(name)

# my solution (worked after modification)
def hello_name(name):
 	return "Hello " + name + "!"

