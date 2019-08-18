from thread import start_new_thread

def squareroot(a):
	eps = 0.0000001
	old = 1
	new = 1
	while True:
		old, new = new , (new + a/new)/ 2.0 
		print(old, new)
		if abs(new - old) < eps:
			break
	return new

start_new_thread(squareroot,(99,))
start_new_thread(squareroot,(999,))
start_new_thread(squareroot,(9999,))

c =  raw_input("Write something to Quit")
