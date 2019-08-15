def factorial(n):
	if n == 0 :
		return 1
	else:
		return n * factorial(n-1)

n = input("Enter the number: ")
fact = factorial(n)
print("Factorial of ", n ," is : ", fact)
