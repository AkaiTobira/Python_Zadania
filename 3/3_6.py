n = int(raw_input("Podaj pierwszy wymiar:"))
k = int(raw_input("Podaj drugi wymiar:"))


output = ""
for j in range(k):
	for i in range(n):
		output += "+---"
	output += "+\n"
	for i in range(n):
		output += "|   "
	output += "|\n"
	
for i in range(n):
		output += "+---"
output += "+"

print output