def fibonacci(n):
	""" Fukcja obbliczajaca n-ty wyraz ciagu Fibonacciego """

	F1,F2,F3 = 1,1,1
	
	if n < 3:
		return 1
	else:
		for i in range(n-2):
			F3 = F2 + F1
			F1 = F2
			F2 = F3
		return F3

print fibonaci(16) # 	987
