import inputUtils

def getPosition(inp):
	position = {'horizontal' : 0, 'depth': 0}
	for each in inp:
		each = each.split(' ')
		#print(each)
		if(each[0] == "forward"):
			position["horizontal"] = position["horizontal"] + int(each[1])
		else:
			if(each[0] == "down"):
				position["depth"] = position["depth"] + int(each[1])
			else:
				position["depth"] = position["depth"] - int(each[1])
	return position

def getAimPosition(inp):
	position = {'horizontal' : 0, 'depth': 0, 'aim': 0}
	for each in inp:
		each = each.split(' ')
		#print(each)
		if(each[0] == "forward"):
			position["horizontal"] = position["horizontal"] + int(each[1])
			position["depth"] = position["depth"] + (int(each[1])*position["aim"])
		else:
			if(each[0] == "down"):
				position["aim"] = position["aim"] + int(each[1])
			else:
				position["aim"] = position["aim"] - int(each[1])
	return position


inp = inputUtils.loadInput(2)

# Part 1
pos = getPosition(inp)
print(pos["depth"] * pos["horizontal"])
# Part 2
pos = getAimPosition(inp)
print(pos["depth"] * pos["horizontal"])
