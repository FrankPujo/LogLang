import sys

# manage sys.argv[] and other inputs
# desired number to find a fraction of
n = float(sys.argv[1])
# maximum
maxc = input( "Enter number of iterations: " )
if maxc == "auto":
	maxc = 100
else:
	maxc = int(maxc)

def main(x, cstop):
	# initialize a and b as 0 and 1
	a = [0, 1]
	b = [1, 1]
	# value for m
	m = [0, 0]
	c = cstop
	# set up some values
	#perfect = False X
	# loop for c iterations
	while c != -1:
		# update m and calculate its value
		m[0] = a[0]+b[0]
		m[1] = a[1]+b[1]
		mv = m[0]/m[1]
		# check if m has desired value or we reached the counter limit
		if x == mv or c == 0:
			# print the equation of the number with the obtained fraction
			print( x, " = ", m[0], "/", m[1], sep="" )
			#perfect = True X
			break
		elif x < mv:
			# if x is smaller than the "median" value (m) then set m as the higher number (b)
			b[0] = m[0]
			b[1] = m[1]
		elif x > mv:
			# if x is smaller than the "median" value (m) then set m as the lower number (a)
			a[0] = m[0]
			a[1] = m[1]
		c -= 1
	# give information about the result
	print( "Reached after:", cstop-c, "iterations." )
	if x == mv:
		#tell if the result is perfect or an approximation
		print( "Perfect result!" )
	else:
		print( "The result is an approximation." )
		print( "Actual value:", mv )
		print( "Percentual difference: ", abs((mv/x)-1)*100, "%", sep="" )

main(n, maxc)