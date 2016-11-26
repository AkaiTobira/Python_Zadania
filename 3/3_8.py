L1 = ["1","53","2","67","31","22","5","5","5","8","2"]
L2 = ["5","53","22","84","212","1","22","5","2","5","5"]

# podpunkt A 
L3 = list()
visited = list()

for item in L1:
	if item in visited:
		continue
	if item in L2:
		L3.append(item)
		visited.append(item)
		
print "a) ", 
print L3


# podpunkt B
L1 = ["1","53","2","67","31","22","5","5","5","8","2"]
L2 = ["5","53","22","84","212","1","22","5","2","5","5"]

L3 = L1 + L2
L4 = list()
for item in L3:
	if item not in L2:
		L4.append(item)

print "b) ",
print L4

