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

measurements = inputUtils.loadInput(1)

print(incrementNum(measurements))