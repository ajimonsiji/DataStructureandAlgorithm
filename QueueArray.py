from ExceptionClass import Empty

class ArrayQueue:
	def __init__(self):
		self._data = []
		self._size = 0
		self._front = 0

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return self._size == 0

	def enqueue(self,e):
		self._data.append(e)
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		value = self._data[self._front]
		self._data[self._front] = None
		self._front = self._front + 1
		self._size = self._size - 1
		return value

	def first(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		return self._data[self._front]	
		

q = ArrayQueue()
print("is_empty() " , q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("Queue : " , q._data)
print("Dequeue : " , q.dequeue())
print("Queue : " , q._data)
print("Length : ", len(q))
print("First : " , q.first())
print("Dequeue : " , q.dequeue())
print("Dequeue : " , q.dequeue())
print("Dequeue : " , q.dequeue())
print("is_empty() " , q.is_empty())
print("First : " , q.first())




