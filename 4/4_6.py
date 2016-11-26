def sum_seq(sequence):
	""" Fukncja zliczajaca sume w sekwencji i podswkwencjach """
	summi = 0
	for item in sequence:
		if isinstance(item,(list,tuple)):
			summi += sum_seq(item)
		else :
			summi += int(item)

	return summi



print sum_seq([1,2,[3,[4,5],[],[6,(7,8,9,10)]]]) #55
