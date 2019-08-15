from ExceptionClass import *

class LinkedList:
	class _Node:
		__slot__ = '_element','_next'
		
		def __init__(self,element,next):
			self._element = element
			self._next = next
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def add_first(self,e):
		newnode = self._Node(e,None)
		if self.is_empty():
			self._head = newnode
			self._tail = newnode
		else:
			newnode._next = self._head
			self._head = newnode
		self._size += 1

	def add_last(self,e):
		newnode = self._Node(e,None)
		if self.is_empty():
			self._head = newnode
			self._tail = newnode
		else:
			self._tail._next = newnode
			self._tail = newnode
		self._size += 1
	def add_any(self, e, pos):
		newnode = self._Node(e,None)
		i = 1
		thead = self._head
		while i < pos:
			thead = thead._next
			i += 1
		newnode._next = thead._next
		thead._next = newnode
		self._size += 1
	
	def remove_first(self):
		if self.is_empty():
			raise Empty("Empty Linked List")
		else:
			value = self._head._element
			self._head = self._head._next
		if self.is_empty():
			self._tail = None
		self._size -= 1
		return value
			
	def remove_last(self):
		if self.is_empty():
                        raise Empty("Empty Linked List")
		i = 0
		print(self._size)
		thead = self._head
		while i < self._size-2:
			thead = thead._next
			i += 1
		value = thead._next._element
		thead._next = None
		self._tail = thead
		return value
		
	def remove_any(self, pos):
		thead = self._head
		i = 1
		thead = self._head
		while i < pos - 1:
			thead = thead._next
			i += 1
		value = thead._next._element
		thead._next = thead._next._next
		self._size -= 1
		return value
		
	
	def display(self):
		thead = self._head
		list = ""
		while thead:
			list = list + str(thead._element) + " -->  "
			thead = thead._next
		print(list)

L = LinkedList()
L.add_first(20)
L.add_first(10)
L.add_last(30)
L.add_last(40)
L.display()
L.add_any(35,3)
L.display()
L.add_first(100)
L.add_last(400)
L.display()
print("remove First")
L.remove_first()
L.display()
print("remove Last")
L.remove_last()
L.display()
L.add_first(10)
L.add_first(10)
L.add_first(10)
L.display()
print("remove Any")
L.remove_any(3)
L.display()
