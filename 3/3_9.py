S = [[],[2,3],(4,8,2),[11],(1,7,9,10)]

L = []
n = 0

for item in S:
	if len(item) == 0:
		L += [0];
	else:
		for item2 in item:
			n += item2
		L += [n]
		n = 0

print L