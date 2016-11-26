

__all__ = [ "factorial", "fibonacci" ]

def factorial(n):
	""" Funkcja liczaca iteracyjnie silnie """
	try:
		ne = int(n)
		result = 1
		for i in range(ne):
			result *= (i+1)
		return result

	except ValueError:
		return 0
	

	

def fibonacci(n):
	""" Fukcja obliczajaca n-ty wyraz ciagu Fibonacciego """

	F1,F2,F3 = 1,1,1
	
	if n < 3:
		return 1
	else:
		for i in range(n-2):
			F3 = F2 + F1
			F1 = F2
			F2 = F3
		return F3


