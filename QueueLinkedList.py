from ExceptionClass import *


class LinkedQueue:
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

	def enqueue(self, e):
		newnode = self._Node(e,self._head)
		if self.is_empty():
			self._head = newnode
			self._tail = newnode
		self._head = newnode
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Empty Stack")
		i = 1
		temp = self._head
		while i < len(self)-1:
			temp = temp._next
			i += 1
		value = self._tail._element
		temp._next = None
		self._tail = temp 
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

	
ls = LinkedQueue()
ls.enqueue(10)
ls.display()
ls.enqueue(20)
ls.display()
ls.enqueue(30)
ls.display()
ls.enqueue(40)
ls.display()
ls.enqueue(60)
ls.display()
v = ls.dequeue()
print("Popelement", v)
ls.display()
print("top",ls.top())
ls.display()
	
			
