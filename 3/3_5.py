n = int(raw_input("Podaj dlugosc miarki: "))

s = ""

for i in range(n):
	s += "|...."
s+= "|\n"

for i in range(n+1):
	if i < 9 : 
		s+= str(i) + "    "
	else :
		s+= str(i) + "   "

s = s[0:len(s)-3]

print s