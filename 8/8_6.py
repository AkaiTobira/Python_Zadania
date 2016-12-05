
P = { (0,0) : 0.5 }

import time

def dynamical(i,j):
	global P
	if (i,j) not in P:
		if i > 0 and j == 0:
			P[(i,j)] = 1.0
			return P[(i,j)]
		elif j > 0 and i == 0:
			P[(i,j)] = 0.0
			return P[(i,j)]
		elif i > 0 and j > 0:
			P[(i,j)] = 0.5 * ( dynamical(i-1,j) + dynamical(i,j-1))
			return P[(i,j)]
	else :
		return P[(i,j)]

def recursive(i,j):
	if i == 0 and j == 0:
		return 0.5
	elif i > 0 and j == 0:
		return 1.0
	elif j > 0 and i == 0:
		return 0.0
	elif i > 0 and j > 0:
		return  0.5 * ( recursive(i-1,j) + recursive(i,j-1))

L = []
A_start = time.time()
for i in range(10):
	L.append([])
	for j in range(21):
		L[i].append(recursive(i,j))
A_stop = time.time()

print A_stop - A_start #12.1884829998  for 210 


L = []
A_start = time.time()
for i in range(1000):
	L.append([])	
	for j in range(6000):
		L[i].append(dynamical(i,j))
A_stop = time.time()

print  A_stop - A_start #11.680314064 for 6000000

