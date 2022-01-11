import requests
import auth

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

def getInput(day):
	# Gets session cookies from private file
	cookies_dict = {"session": auth.getCookies()}
	url = "https://adventofcode.com/2021/day/" + str(day) + "/input"
	req = requests.get(url, cookies=cookies_dict)
	if(day < 10):
		day = "0" + str(day)
	filename = str(day) + ".txt"
	with open("inputs/" + filename, "w") as f:
		f.write(req.text)
	print(f"Input day {day} fetched")

def getAllInputs():
	for i in range(1, 26):
		getInput(i)

def createPyFiles():
	for day in range(1,26):
		if(day < 10):
			day = "0" + str(day)
		filename = str(day) + ".py"
		with open(filename, "w") as f:
			f.write("import inputUtils")
		print(f"Python file day {day} created")
