HELLO_WORLD = "HI!"

class Person:

	f_name = ''
	l_name = ''

	def print_name(self):
		print '%s %s' % (self.f_name, self.l_name)

class ZackPerson(Person):
	f_name = 'Zack'
	l_name = 'Fazio'


class AdamPerson(Person):

	f_name = 'Adam'
	l_name = 'Jarvis'

	def print_name(self):
		print '%s %s, King of the Word' % (self.f_name, self.l_name)