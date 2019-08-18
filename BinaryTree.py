from ExceptionClass import *
from QueueLinkedList import *



class BinaryTree:
	class _Node:
		__slot__ = '_element','_left','_right'
		def __init__(self,e, left=None,right=None):
			self._element = e
			self._left = left
			self._right = right
	def __init__(self):
		self._root = None
		self._size = 0

	def maketree(self,e,left,right):
		self._root = self._Node(e,left._root,right._root)
		left._root = None
		right._root = None

	def levelorder(self):
		Q = LinkedQueue()
		t = self._root
		print(t._element, '--')
		Q.enqueue(t)
		while not Q.is_empty():
			t = Q.dequeue()
			if t._left:
				print(t._left._element,'--')
				Q.enqueue(t._left)
			if t._right:
                                print(t._right._element,'--')
                                Q.enqueue(t._right)
	def inorder(self,troot):
		if troot:
			self.inorder(troot._left)
			print(troot._element,'--')
			self.inorder(troot._right)
		
	def preorder(self,troot):
                if troot:
                        print(troot._element,'--')
                        self.preorder(troot._left)
                        self.preorder(troot._right)	
			 
	def postorder(self,troot):
                if troot:
                        self.postorder(troot._left)
                        self.postorder(troot._right)
                        print(troot._element,'--')


a = BinaryTree()
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()


x.maketree(40,a,a)
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,y)
s.maketree(30,r,a)
t.maketree(10,z,x)


t.levelorder()
print()
t.inorder(t._root)
print()
t.postorder(t._root)
print()
t.preorder(t._root)
print()
