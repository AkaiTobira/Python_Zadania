val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
key  =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
# dwuznak to klucz skladajacy sie z dwoch charow

def roman2int( smt ):

	D = dict(zip(key,val))
	exp,index = 0,0
	smt += " "
	for i in range(len(smt)-1) :
		if index <= i :
			if D.has_key(smt[i:i+2]):				
				exp += D[smt[i:i+2]]
				index +=2
			else: 
				exp+=D[smt[i]]
				index +=1
	return exp 

	
def int2roman( vari ):
	D = dict(zip(val,key))
	if vari <= 0 :
		return "0"
	result = 0
	exp = ""
	while result < vari:
		for inte in val:
			while result + inte <= vari:
				exp += D[inte]
				result += inte

	return exp 

for i in range (2000):
	if not roman2int(int2roman(i+1)) == i+1:
		print "Nie dziala dla : ",str(i+1)
