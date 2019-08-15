from ExceptionClass import Empty

class ArrayStack:
	def __init__(self):
		self._data = []
	def __len__(self):
		return len(self._data)
	def is_empty(self):
		return len(self._data) == 0
	def push(self,e):
		self._data.append(e)
	def pop(self):
		if self.is_empty():
			raise Empty("Stack is Empty")
		return self._data.pop()

	def top(self):
		if self.is_empty():
			raise Empty("Stack is Empty")
	 	return self._data[-1]	


s = ArrayStack()
s.push(10)
s.push(20)
print("stack : ",s._data)
print("stack len : " , len(s))
print("Is_empty", s.is_empty())
print("top: ", s.top())
s.push(30)
print("stack : ",s._data)
print("pop",s.pop())
print("top: ", s.top())
print("stack : ",s._data)
print("pop",s.pop())
print("pop",s.pop())
print("Is_empty", s.is_empty())
