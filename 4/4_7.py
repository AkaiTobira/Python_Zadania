def flatten(sequence):
	"""Funkcja zamieniająca sekwencje z sekwencjami o roznych poziomach zagniezdzenia do jednej sekwencji ze wszystkimi elementami """
	L = []
	for item in sequence:
		if isinstance(item,(list,tuple)):
			L += flatten(item)
		else:
			L.append(item)
	return L




seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(seq)            # [1,2,3,4,5,6,7,8,9]
