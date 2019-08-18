import os

def child():
	print("\n A New Child ", os.getpid())
	os._exit(0)

def parent():
	while True:
		newpid = os.fork()
		if newpid == 0:
			child()
		else:
			pids = (os.getpid(), newpid)
			print("\nParent %s, child %s " %(pids))
		reply = raw_input("q for Quit/ c for Continue: ")
		print(reply)
		if reply == "c":
			continue
		elif reply == "q":
			break
		else:
			print("Enter q/c ")

parent()
