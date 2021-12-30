import inputUtils


def getRates(l):
	matrix = [[int(i) for i in list(each)] for each in l]
	
	column = [sum([row[i] for row in matrix]) for i in range(0, len(matrix[0]))]
	gamma = "".join(["1" if value > (len(l)/2) else "0" for value in column])
	#column = int(column)
	epilson = "".join(["0" if value == "1" else "1" for value in gamma])
	return int(gamma, 2), int(epilson, 2)

def getPowerConsumption(l):
	gamma, epilson = getRates(l)
	return gamma*epilson


inp = inputUtils.loadInput(3)
print(getPowerConsumption(inp))