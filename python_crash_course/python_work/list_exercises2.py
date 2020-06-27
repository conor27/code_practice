# make a list of three famous people to invite to dinner

famous_people = ['john lennon', 'albert einstein', 'elon musk']

print(f'Hi {famous_people[0].title()}, would you like to come to dinner?')
print(f'Hi {famous_people[1].title()}, would you like to come to dinner?')
print(f'Hi {famous_people[2].title()}, would you like to come to dinner?\n')

print(f"{famous_people[1].title()} can't make it!\n")

famous_people[1] = 'steve jobs'

print(f'Hi {famous_people[0].title()}, please come for dinner!')
print(f'Hi {famous_people[1].title()}, please come for dinner!')
print(f'Hi {famous_people[2].title()}, please come for dinner!\n')

print(f'Table is bigger than we realized. Some extra people will be added.\n')

famous_people.insert(0, 'joe rogan')
famous_people.insert(2, 'kevin hart')
famous_people.append('lionel messi')

print(f'{famous_people[0].title()}, dinner?')
print(f'{famous_people[1].title()}, dinner?')
print(f'{famous_people[2].title()}, dinner?')
print(f'{famous_people[3].title()}, dinner?')
print(f'{famous_people[4].title()}, dinner?')
print(f'{famous_people[5].title()}, dinner?\n')

print("Oof. It actually looks like the table isn't coming after all. Big cuts coming.\n")

print(f"Sorry {famous_people.pop().title()}, but the table's full.")
print(f"Sorry {famous_people.pop().title()}, but the table's full.")
print(f"Sorry {famous_people.pop().title()}, but the table's full.")
print(f"Sorry {famous_people.pop().title()}, but the table's full.\n")

print(f"Don't worry {famous_people[0].title()}, you're still invited.")
print(f"Don't worry {famous_people[1].title()}, you're still invited.\n")

print(f"At this point, it looks like {len(famous_people)} people will be invited for dinner.\n")

del famous_people[1]
del famous_people[0]

print(famous_people)




