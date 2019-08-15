def BinarySearch(A,key):
	low = 0
	high = len(A)
	while low <= high:
		mid = (low + high)/2
		if A[mid] == key:
			return True
		elif A[mid] < key:
			low = mid + 1
		else:
			high = mid - 1
	return False

A = [4,11,18,30,54,96]
key = 96
found = BinarySearch(A,key)
print("Key ",key," is Present :", found)
