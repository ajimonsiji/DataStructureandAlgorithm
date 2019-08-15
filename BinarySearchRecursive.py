def BinarySearchRecursive(A,low,high,key):
	if low > high:
		return False
	else:
		mid = (low + high)/2
		if A[mid] == key:
			return True
		elif A[mid] < key:
			return BinarySearchRecursive(A,mid+1,high,key)
		else:
			return BinarySearchRecursive(A,low,mid-1,key)

A = [1,2,3,4,5,6,7,8]
key = 18
found = BinarySearchRecursive(A,0,7,key)
print("Key is present ", found)
	
	
