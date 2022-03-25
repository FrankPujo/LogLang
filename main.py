import sys

filename = sys.argv[1]
sourceCode = open( filename, 'r' ).read()

lines = sourceCode.split( "\n" )
