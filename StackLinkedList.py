from ExceptionClass import *


class LinkedStack:
	class _Node:
		__slot__ = '_element','_next'
		def __init__(self, element, next):
			self._element = element
			self._next = next
	def __init__(self):
		self._head = None
		self._size = 0 
	
	def is_empty(self):
		return self._size == 0

	def __len__(self):
		return self._size

	def push(self, e):
		newnode = self._Node(e,self._head)
		self._head = newnode
		self._size += 1

	def pop(self):
		if self.is_empty():
			raise Empty("Empty Stack")
		value = self._head._element
		self._head = self._head._next
		self._size -= 1
		return value

	def top(self):
		if self.is_empty():
                        raise Empty("Empty Stack")
		return self._head._element

	def display(self):
		temp = self._head
		list = ""
		while temp:
			list = list + "-->" + str(temp._element)
			temp = temp._next
		print(list)

	
ls = LinkedStack()
v = ls.pop()
ls.push(10)
ls.push(20)
ls.push(30)
ls.push(40)
ls.push(60)
ls.display()
v = ls.pop()
print("Popelement", v)
print("top",ls.top())
ls.display()
	
			
