def foo(print_this, and_this):
	print "%s" % and_this
	print "%s" % and_this

foo("Hello, Adam", "Hello, Jack")

class PrintName:
	def __init__(self):
		pass

our_name_object = PrintName()
print '%s' % our_name_object