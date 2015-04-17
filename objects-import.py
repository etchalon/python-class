from people import ZackPerson, AdamPerson, HELLO_WORLD

people = [
	ZackPerson(),
	AdamPerson(),
	ZackPerson(),
	AdamPerson(),
	ZackPerson(),
	AdamPerson(),
	ZackPerson(),
	AdamPerson(),
]

people[4].f_name = 'Jack'

for person in people:
	person.print_name()
