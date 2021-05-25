import sys

filename = sys.argv[1]
sourceCode = open( filename, 'r' ).read()

lines = sourceCode.split( "\n" )

for lineNum in range(len(lines)):
	if lineNum == 0:
		lineArr = []
		firstLine = lines[0]
		numbers = firstLine.split( " " )
		for number in numbers:
			digits = list( number )
			lineArr.append( digits )
