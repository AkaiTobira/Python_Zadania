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
	

	


print factorial(3) 		#6
print factorial("ji")		#0
