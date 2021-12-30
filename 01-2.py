import inputUtils

def getPreviousList(l):
	return [l[0]] + l[0:-1]

def convertToInt(l):
	return [int(i) for i in l]

def incrementsOnSlidingWindow(l):
	l = convertToInt(l)
	window = [l[i] + l[i+1] + l[i+2] for i in range(0, len(l)-2)]
	prev = getPreviousList(window)
	# Increment if previous is smaller than current
	increment = [1 if (window[i] - prev[i]) > 0 else 0 for i in range(0, len(window))]
	return(sum(increment))

measurements = inputUtils.loadInput(1)
print(incrementsOnSlidingWindow(measurements))