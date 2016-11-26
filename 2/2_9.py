
infile = open("test", "r" )
outfile = open("output","w")

while True :
	S = infile.readline();
	if  "#" not in S :
		outfile.write(S)
	if  S == "" : 
		break

infile.close()
outfile.close()
