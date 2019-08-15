class parent():
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	
	def printname(self):
		print(self.fname, self.lname)



class childclass(parent):
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		super().printname()

	


x = childclass("ajimon","siji")
x.printname()
