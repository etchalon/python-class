hello = "Hello"

class PrintString:
	def __init__(self):
		self.counter = 0
	def init(self):
		self.counter = 100
	def print_counter(self):
		print "%s" % self.counter
		self.counter += 1

class PrintNothing:
	pass

instance_1 = PrintString()
instance_2 = PrintString()
instance_3 = PrintNothing()

instance_1.print_counter()
instance_1.print_counter()
instance_1.print_counter()
instance_1.init()
instance_1.print_counter()
instance_1.print_counter()
instance_1.print_counter()


print isinstance(instance_1, PrintNothing)
print isinstance(instance_1, PrintString)