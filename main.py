import sys

filename = sys.argv[1]
sourceCode = open( filename, 'r' ).read()

lines = sourceCode.split( "\n" )

# variables dictionary
variables = {}

for line in lines:
	tokens = line.split(" ")
	keyword = tokens[0]
	# handle variable declarations
	if keyword == "loc":
		# find variable name
		name = tokens[1]
		lastT = len(tokens)
		# find the value of the variable after the ">" symbol
		iValue = ' '.join(x for x in tokens[3:lastT])
		fValue = ""
		# for each character swap to python syntax
		# get variable values from the variable dictionary
		for e in iValue.split(" "):
			eV = e
			if e == "^":
				eV = "&"
			elif e == "V":
				eV = "|"
			elif e == "°":
				eV = "~"
			elif e != "0" and e != "1":
				eV = variables.get(e)
			eV = str(eV) + " "
			fValue += eV
		# evaluate the value from python syntax
		aValue = eval( fValue )
		# insert variable's name and value inside the dictionary
		variables.update( { name: aValue } )

print( variables )