def loadInput(day):
	if(day < 10):
		day = "0" + str(day)
	filename = str(day) + ".txt"
	with open("inputs/" + filename) as f:
		content = [l[:-1] if l[-1] == "\n" else l for l in f.readlines()]

	if len(content) == 1:
		try:
			return content[0]
		except:
			try:
				return [i for i in content[0].split()]
			except:
				return content[0]
	else:
		try:
			return [i for i in content]
		except:
			return content