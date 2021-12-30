import inputUtils
def getPreviousList(l):
	return [l[0]] + l[0:-1]

def convertToInt(l):
	return [int(i) for i in l]

def incrementNum(l):
	l = convertToInt(l)
	prev = getPreviousList(l)
	
	# Increment if previous is smaller than current
	increment = [1 if (int(l[i]) - int(prev[i])) > 0 else 0 for i in range(0, len(l))]
	return sum(increment)

def incrementsOnSlidingWindow(l):
	l = convertToInt(l)
	window = [l[i] + l[i+1] + l[i+2] for i in range(0, len(l)-2)]
	prev = getPreviousList(window)
	# Increment if previous is smaller than current
	increment = [1 if (window[i] - prev[i]) > 0 else 0 for i in range(0, len(window))]
	return(sum(increment))

	
measurements = inputUtils.loadInput(1)

# Part 1
print(incrementNum(measurements))
# Part 2
print(incrementsOnSlidingWindow(measurements))