while True:
	n = raw_input("Podaj wartosc lub zakoncz piszac stop: ")
	if "stop" in n :
		break
	else:
		try:
			print n + " " +  str(float(n)**3) 
		except ValueError:
			pass
	