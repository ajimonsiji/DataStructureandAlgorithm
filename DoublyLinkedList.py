from ExceptionClass import *

class DoublyLinkedList:
	__slot__ = '_element','_pre','_next'
	class _Node:
		def __init__(self, element, pre, next):
			self._element = element
			self._pre = pre
			self._next = next
	
	def __init__(self):
		self._size = 0
		self._head = None
		self._tail = None

	def is_empty(self):
		return self._size ==0

	def __len__(self):
		return self._size

	def add_first(self, e):
		newnode = self._Node(e, None,None)
		if self.is_empty():
			self._head = newnode
			self._tail = newnode
		else:
			self._head._pre = newnode
			newnode._next = self._head
			self._head = newnode
		self._size += 1

	def add_last(self, e):
		newnode = self._Node(e,None,None)
		if self.is_empty():
			self._head = newnode
                        self._tail = newnode
		else:
			self._tail._next = newnode
			newnode._pre = self._tail
			self._tail = newnode
		self._size += 1
 	def add_any(self, e , pos):
		newnode = self._Node(e, None, None)
		if self.is_empty():
			self._head = newnode
                        self._tail = newnode 
		i = 0
		thead = self._head
		while i < pos :
			thead = thead._next
			i += 1
		thead._next._pre = newnode
		newnode._pre = thead
		newnode._next = thead._next
		thead._next = newnode	
		self._size += 1
				
	def display(self):
		thead = self._head
		list = ""
		while thead:
			list = list + str(thead._element) + " -->  "
			thead = thead._next
		print(list)
	def remove_first(self):
		if self.is_empty():
			raise Empty("Empty Doubly linkedList")
		value = self._head._element
		thead = self._head._next
		thead._pre = None
		self._head = thead
		self._size -= 1
		return value

	def remove_last(self):
		if self.is_empty():
                        raise Empty("Empty Doubly linkedList")
		value = self._tail._element
		thead = self._tail._pre
		thead._next = None
		self._tail = thead
		self._size -= 1
		return value
		
	def remove_any(self, pos):
		if self.is_empty():
                        raise Empty("Empty Doubly linkedList")
		i = 1
		thead = self._head
		while i < pos - 2:
			thead = thead._next
		value = thead._next._element
		thead._next = thead._next._next
		thead._next._pre = thead
		self._size -= 1
		return value
		
L = DoublyLinkedList()
L.add_first(10)
L.add_last(20)
L.add_first(1)
L.add_last(30)
L.add_any(15,2)
L.display()
L.remove_first()
print("remove First")
L.display()
L.remove_last()
L.display()
L.remove_any(2)
print("Remove any")
L.display()
