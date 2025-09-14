def factorial(x):
	i=0
	fact=1
	for i in range(1,x+1):
		fact*=i
	return fact

#main
n=int(input("Enter a number: "))
print(f"Factorial of {n} is: {factorial(n)}")