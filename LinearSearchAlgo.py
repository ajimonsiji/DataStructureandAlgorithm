"""Linear Search Algorithm"""

def LinearSearchAlgorithm(A,key):
	position = 0
	flag = False
	while len(A) > position and not flag:
		if A[position] == key:
			flag = True
		else:
			position = position + 1
	return flag,position

A = [84,56,74,23,56,11,2,89]
found,position = LinearSearchAlgorithm(A,41)
print("Element 11 present : " , found )
 
