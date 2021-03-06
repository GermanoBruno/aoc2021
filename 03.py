import inputUtils
import pandas as pd

def getRates(l):
	matrix = [[int(i) for i in list(each)] for each in l]
	
	column = [sum([row[i] for row in matrix]) for i in range(0, len(matrix[0]))]
	gamma = "".join(["1" if value > (len(l)/2) else "0" for value in column])
	#column = int(column)
	epilson = "".join(["0" if value == "1" else "1" for value in gamma])
	return int(gamma, 2), int(epilson, 2)


def getRatings(l):
	matrix = [[int(i) for i in list(each)] for each in l]
	df = pd.DataFrame(matrix)
	oxygen = ""
	for i in df.columns:
		if(df[i].value_counts()[0] == df[i].value_counts()[1]):
			mostFreq = 1
		else:
			mostFreq = df[i].value_counts().index[0]
		oxygen = oxygen + str(mostFreq)
		df = df.drop(df.loc[df[i] != mostFreq].index)
	df = pd.DataFrame(matrix)
	co2 = ""
	for i in df.columns:
		if(len(df[i].value_counts()) > 1):
			if(df[i].value_counts()[0] == df[i].value_counts()[1]):
				leastFreq = 0
			else:
				leastFreq = df[i].value_counts().index[1]
			co2 = co2 + str(leastFreq)
			df = df.drop(df.loc[df[i] != leastFreq].index)
		else:
			co2 = "".join([str(i) for i in df.values[0]])
#		print(df[i].value_counts())

	return int(oxygen,2), int(co2, 2)


def getLifeSupportRating(l):
	oxygen, co2 = getRatings(l)
	return oxygen*co2

def getPowerConsumption(l):
	gamma, epilson = getRates(l)
	return gamma*epilson

inp = inputUtils.loadInput(3)

# Part 1
print(getPowerConsumption(inp))
# Part 2
print(getLifeSupportRating(inp))
