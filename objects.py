people = [
	{
		'f_name': "Adam",
		'l_name': 'Jarvis'
	},
	{
		'f_name': "Zack",
		'l_name': 'Fazio'
	},
]

def print_name(person):
	print '%s %s' % (person['f_name'], person['l_name'])

print_name(people[0])
print_name(people[1])