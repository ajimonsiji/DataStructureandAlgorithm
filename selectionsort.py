
def selectionsort(A):
	l = len(A)
	for i in range(l-1,0,-1):
		max_pos = 0
		for j in range(1,i+1):
			if A[j] > A[max_pos]:
				max_pos = j
		temp = A[i]
		A[i] = A[max_pos]
		A[max_pos] = temp 

A = [84,21,96,15,47]
print("Original Array :",A)
selectionsort(A)
print("Sorted Array :",A)

